"""BPMN 2.0 tooling (bpmn_tool.py), shipped BPMN diagrams, and wide diagrams in Word export."""
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zipfile
import zlib
import xml.etree.ElementTree as ET
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import bpmn_tool  # noqa: E402
import md_to_docx  # noqa: E402

BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
BPMNDI = "{http://www.omg.org/spec/BPMN/20100524/DI}"

SPEC = {
    "id": "duyet",
    "name": "Duyệt đề nghị",
    "pool": "Công ty",
    "lanes": [{"id": "nv", "name": "Nhân viên"}, {"id": "ql", "name": "Quản lý"}],
    "nodes": [
        {"id": "start", "type": "start", "name": "Cần mua vật tư", "lane": "nv"},
        {"id": "t1", "type": "user", "name": "Tạo đề nghị", "lane": "nv"},
        {"id": "t2", "type": "user", "name": "Duyệt đề nghị", "lane": "ql"},
        {"id": "timer", "type": "boundary_timer", "name": "Quá 24 giờ", "attached_to": "t2", "interrupting": False},
        {"id": "t_nhac", "type": "send", "name": "Nhắc Quản lý", "lane": "ql", "row": 1},
        {"id": "e_nhac", "type": "end", "name": "Đã nhắc", "lane": "ql", "row": 1},
        {"id": "g1", "type": "xor", "name": "Đồng ý?", "lane": "ql"},
        {"id": "e_ok", "type": "end", "name": "Đề nghị được duyệt", "lane": "ql"},
        {"id": "e_no", "type": "end", "name": "Đề nghị bị từ chối", "lane": "nv"},
    ],
    "flows": [
        ["start", "t1"], ["t1", "t2"], ["timer", "t_nhac"], ["t_nhac", "e_nhac"],
        ["t2", "g1"], ["g1", "e_ok", "Đồng ý"], ["g1", "e_no", "Từ chối"],
    ],
}


def model(spec=None):
    return bpmn_tool.model_from_spec(json.loads(json.dumps(spec or SPEC)))


def problems(spec):
    return bpmn_tool.validate(model(spec))


def wide_png(width: int, height: int) -> bytes:
    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    raw = b"".join(b"\x00" + b"\xff\xff\xff" * width for _ in range(height))
    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


class BpmnBuildTests(unittest.TestCase):
    def test_spec_builds_standard_bpmn_with_layout(self):
        self.assertEqual(problems(SPEC), ([], []))
        root = ET.fromstring(bpmn_tool.to_xml(model()).encode("utf-8"))
        process = root.find(f"{BPMN}process")
        self.assertEqual(len(process.findall(f"{BPMN}laneSet/{BPMN}lane")), 2)
        self.assertEqual(process.find(f"{BPMN}task[@id='t1']").get("name"), "Tạo đề nghị")
        self.assertIsNone(process.find(f"{BPMN}userTask"))  # no task icons by default
        with_icons = json.loads(json.dumps(SPEC))
        with_icons["task_icons"] = True
        self.assertIn('<bpmn:userTask id="t1"', bpmn_tool.to_xml(model(with_icons)))
        boundary = process.find(f"{BPMN}boundaryEvent")
        self.assertEqual((boundary.get("attachedToRef"), boundary.get("cancelActivity")), ("t2", "false"))
        self.assertIsNotNone(boundary.find(f"{BPMN}timerEventDefinition"))
        flows = process.findall(f"{BPMN}sequenceFlow")
        self.assertEqual(len(flows), 7)
        plane = root.find(f"{BPMNDI}BPMNDiagram/{BPMNDI}BPMNPlane")
        shapes = {shape.get("bpmnElement") for shape in plane.findall(f"{BPMNDI}BPMNShape")}
        self.assertTrue({"t1", "t2", "g1", "nv", "ql", "timer"} <= shapes)
        edges = plane.findall(f"{BPMNDI}BPMNEdge")
        self.assertEqual(len(edges), 7)
        self.assertTrue(all(len(edge.findall("{http://www.omg.org/spec/DD/20100524/DI}waypoint")) >= 2 for edge in edges))

    def test_build_then_check_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            spec = Path(tmp) / "duyet.json"
            spec.write_text(json.dumps(SPEC, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(bpmn_tool.main(["build", str(spec)]), 0)
            self.assertEqual(bpmn_tool.main(["check", str(Path(tmp) / "duyet.bpmn"), "--strict"]), 0)

    def test_model_errors_block_the_build(self):
        broken = json.loads(json.dumps(SPEC))
        broken["flows"] = [f for f in broken["flows"] if f != ["g1", "e_no", "Từ chối"]] + [["g1", "e_no"]]
        errors, _ = problems(broken)
        self.assertTrue(any("thiếu điều kiện" in e for e in errors))
        with tempfile.TemporaryDirectory() as tmp:
            spec = Path(tmp) / "loi.json"
            spec.write_text(json.dumps(broken, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(bpmn_tool.main(["build", str(spec)]), 1)
            self.assertFalse((Path(tmp) / "loi.bpmn").exists())

    def test_structural_errors(self):
        dangling = json.loads(json.dumps(SPEC))
        dangling["nodes"].append({"id": "lac", "type": "task", "name": "Bước lạc", "lane": "nv"})
        errors, _ = problems(dangling)
        self.assertTrue(any("lac" in e and "không có luồng vào" in e for e in errors))
        self.assertTrue(any("lac" in e and "không có luồng ra" in e for e in errors))
        no_lane = json.loads(json.dumps(SPEC))
        no_lane["nodes"][1]["lane"] = "khong_co"
        self.assertTrue(any("không thuộc lane" in e for e in problems(no_lane)[0]))
        bad_ref = json.loads(json.dumps(SPEC))
        bad_ref["flows"].append(["t1", "khong_ton_tai"])
        self.assertTrue(any("không tồn tại" in e for e in problems(bad_ref)[0]))
        loose_boundary = json.loads(json.dumps(SPEC))
        loose_boundary["nodes"][3]["attached_to"] = "g1"
        self.assertTrue(any("sự kiện biên" in e for e in problems(loose_boundary)[0]))
        with self.assertRaises(ValueError):
            bad_type = json.loads(json.dumps(SPEC))
            bad_type["nodes"][1]["type"] = "loai_la"
            model(bad_type)

    def test_modelling_warnings(self):
        statement = json.loads(json.dumps(SPEC))
        statement["nodes"][6]["name"] = "Quyết định"
        self.assertTrue(any("câu hỏi" in w for w in problems(statement)[1]))
        unpaired = json.loads(json.dumps(SPEC))
        unpaired["nodes"].append({"id": "p1", "type": "and", "lane": "ql"})
        unpaired["flows"] = [f for f in unpaired["flows"] if f[0] != "g1"] + [["g1", "p1", "Đồng ý"], ["g1", "e_no", "Từ chối"], ["p1", "e_ok"], ["p1", "e_nhac"]]
        self.assertTrue(any("song song" in w for w in problems(unpaired)[1]))

    def test_highlight_uses_bpmn_io_colour_extension(self):
        coloured = json.loads(json.dumps(SPEC))
        coloured["nodes"][1]["highlight"] = "pain"
        xml = bpmn_tool.to_xml(model(coloured))
        self.assertIn('bpmnElement="t1" bioc:stroke="#C53030"', xml)


class ShippedBpmnTests(unittest.TestCase):
    def test_sample_diagrams_are_valid_and_match_their_spec(self):
        folders = [ROOT / "BA-Documents-Outsource" / "diagrams", ROOT / "BA-Documents-Product" / "diagrams", ROOT / "diagrams"]
        files = [path for folder in folders for path in sorted(folder.glob("*.bpmn"))]
        self.assertGreaterEqual(len(files), 13)
        for path in files:
            errors, warnings = bpmn_tool.validate(bpmn_tool.model_from_bpmn(path))
            self.assertEqual((errors, warnings), ([], []), path.name)
            spec = path.with_suffix(".json")
            if spec.exists():
                rebuilt = bpmn_tool.to_xml(bpmn_tool.model_from_spec(json.loads(spec.read_text(encoding="utf-8"))))
                self.assertEqual(rebuilt, path.read_text(encoding="utf-8"), f"{path.name} is stale: rebuild from {spec.name}")
            self.assertTrue(path.with_suffix(".png").exists(), f"{path.name} has no exported PNG")

    def test_documents_link_the_bpmn_source_next_to_each_image(self):
        docs = [
            ROOT / "BA-Documents-Outsource" / "02-BRD.md",
            ROOT / "BA-Documents-Outsource" / "04-Process-Flow.md",
            ROOT / "BA-Documents-Product" / "02-BRD.md",
            ROOT / "BA-Documents-Product" / "04-User-Flow.md",
            ROOT / "so_do.md",
        ]
        for doc in docs:
            text = doc.read_text(encoding="utf-8")
            images = [line for line in text.splitlines() if line.startswith("![") and "diagrams/" in line]
            self.assertTrue(images, doc.name)
            for line in images:
                stem = line.split("diagrams/")[1].split(".png")[0]
                self.assertIn(f"diagrams/{stem}.bpmn", text, f"{doc.name}: {stem}")
                self.assertTrue((doc.parent / "diagrams" / f"{stem}.png").exists())

    @unittest.skipUnless(
        shutil.which("node") and os.environ.get("BA_BPMN_NODE_MODULES"),
        "render needs Node.js and BA_BPMN_NODE_MODULES pointing to bpmn-js + puppeteer-core",
    )
    def test_bpmn_js_imports_a_built_diagram_without_warnings(self):
        with tempfile.TemporaryDirectory() as tmp:
            bpmn = Path(tmp) / "duyet.bpmn"
            bpmn.write_text(bpmn_tool.to_xml(model()), encoding="utf-8")
            code, message = bpmn_tool.render(bpmn, Path(tmp) / "duyet.svg", os.environ.get("BA_MERMAID_BROWSER"))
            self.assertEqual(code, 0, message)


class WideDiagramWordTests(unittest.TestCase):
    def test_wide_picture_gets_its_own_landscape_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "diagrams").mkdir()
            (root / "diagrams" / "rong.png").write_bytes(wide_png(1600, 600))
            (root / "diagrams" / "hep.png").write_bytes(wide_png(400, 300))
            md = root / "doc.md"
            md.write_text("# Quy trình\n\n![Rộng](diagrams/rong.png)\n\nGiữa\n\n![Hẹp](diagrams/hep.png)\n", encoding="utf-8")
            counts = md_to_docx.convert(md, root / "doc.docx")
            self.assertEqual(counts["landscape_pages"], 1)
            with zipfile.ZipFile(root / "doc.docx") as zf:
                document = zf.read("word/document.xml").decode("utf-8")
            self.assertEqual(document.count('w:orient="landscape"'), 1)
            self.assertEqual(document.count("<w:sectPr"), 3)  # portrait break, landscape break, final section
            self.assertEqual(document.count("<w:drawing>"), 2)


if __name__ == "__main__":
    unittest.main()
