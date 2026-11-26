"""BPMN 2.0 tooling (bpmn_tool.py), shipped BPMN diagrams, and wide diagrams in Word export."""
import json
import os
import re
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


    def test_ids_are_valid_and_unique(self):
        digits = json.loads(json.dumps(SPEC))
        digits["nodes"][1]["id"] = "1"
        digits["flows"] = [["start", "1"] if f == ["start", "t1"] else (["1", "t2"] if f == ["t1", "t2"] else f) for f in digits["flows"]]
        xml = bpmn_tool.to_xml(model(digits))
        self.assertIn('<bpmn:task id="_1"', xml)
        lane_clash = json.loads(json.dumps(SPEC))
        lane_clash["lanes"].append({"id": "n v", "name": "Nhân viên 2"})  # "n v" and "n_v" would both become n_v
        lane_clash["lanes"].append({"id": "n_v", "name": "Nhân viên 3"})
        with self.assertRaisesRegex(ValueError, "trùng"):
            model(lane_clash)
        node_vs_flow = json.loads(json.dumps(SPEC))
        node_vs_flow["nodes"][1]["id"] = "Flow_1"
        node_vs_flow["flows"] = [["start", "Flow_1"] if f == ["start", "t1"] else (["Flow_1", "t2"] if f == ["t1", "t2"] else f) for f in node_vs_flow["flows"]]
        with self.assertRaisesRegex(ValueError, "trùng"):
            model(node_vs_flow)

    def test_bad_specs_exit_2_without_traceback(self):
        no_lanes = json.loads(json.dumps(SPEC))
        no_lanes["lanes"] = []
        cases = {"lanes.json": no_lanes, "short.json": {**SPEC, "flows": [["start"]]}, "list.json": [SPEC]}
        with tempfile.TemporaryDirectory() as tmp:
            for name, spec in cases.items():
                path = Path(tmp) / name
                path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
                self.assertIn(bpmn_tool.main(["build", str(path)]), (1, 2), name)
            self.assertEqual(bpmn_tool.main(["check", tmp]), 2)  # no .bpmn in the folder
            (Path(tmp) / "hong.bpmn").write_text("<bpmn:definitions", encoding="utf-8")
            self.assertEqual(bpmn_tool.main(["check", str(Path(tmp) / "hong.bpmn")]), 2)

    def test_layout_is_repeatable_and_respects_requested_rows(self):
        spec = json.loads(json.dumps(SPEC))
        built = model(spec)
        self.assertEqual(bpmn_tool.to_xml(built), bpmn_tool.to_xml(built))
        crowded = {
            "id": "c", "name": "c", "pool": "p", "lanes": [{"id": "a", "name": "A"}],
            "nodes": [
                {"id": "s", "type": "start", "name": "Bắt đầu", "lane": "a"},
                {"id": "p1", "type": "and", "lane": "a"},
                {"id": "t1", "type": "task", "name": "Một", "lane": "a"},
                {"id": "t2", "type": "task", "name": "Hai", "lane": "a", "row": 0},
                {"id": "p2", "type": "and", "lane": "a"},
                {"id": "e", "type": "end", "name": "Xong", "lane": "a"},
            ],
            "flows": [["s", "p1"], ["p1", "t1"], ["p1", "t2"], ["t1", "p2"], ["t2", "p2"], ["p2", "e"]],
        }
        laid = model(crowded)
        bpmn_tool.layout(laid)
        self.assertNotEqual((laid.nodes["t1"].x, laid.nodes["t1"].y), (laid.nodes["t2"].x, laid.nodes["t2"].y))
        self.assertEqual(laid.nodes["t2"].row, 0)

    def test_check_reads_what_modelers_save(self):
        xml = """<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" id="d">
  <collaboration id="c">
    <participant id="p1" name="Khách" processRef="A" /><participant id="p2" name="Cửa hàng" processRef="B" />
  </collaboration>
  <process id="A">
    <startEvent id="a_s" name="Bắt đầu" />
    <eventBasedGateway id="a_g" />
    <intermediateCatchEvent id="a_m" name="Nhận thư"><messageEventDefinition id="a_md" /></intermediateCatchEvent>
    <intermediateCatchEvent id="a_t" name="Quá 1 ngày"><timerEventDefinition id="a_td" /></intermediateCatchEvent>
    <endEvent id="a_e" name="Xong" />
    <sequenceFlow id="f1" sourceRef="a_s" targetRef="a_g" /><sequenceFlow id="f2" sourceRef="a_g" targetRef="a_m" />
    <sequenceFlow id="f3" sourceRef="a_g" targetRef="a_t" /><sequenceFlow id="f4" sourceRef="a_m" targetRef="a_e" />
    <sequenceFlow id="f5" sourceRef="a_t" targetRef="a_e" />
  </process>
  <process id="B">
    <startEvent id="b_s" name="Bắt đầu" /><task id="b_t" name="Bước lạc" /><endEvent id="b_e" name="Xong" />
    <sequenceFlow id="g1" sourceRef="b_s" targetRef="b_e" />
  </process>
</definitions>"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "hai-pool.bpmn"
            path.write_text(xml, encoding="utf-8")
            first, second = bpmn_tool.models_from_bpmn(path)
            self.assertEqual(bpmn_tool.validate(first)[0], [])  # event-based gateway is understood
            self.assertTrue(any("b_t" in e for e in bpmn_tool.validate(second)[0]))  # second pool is checked too
            self.assertEqual(bpmn_tool.main(["check", str(path)]), 1)

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

    def test_no_flow_is_drawn_through_another_element(self):
        folders = [ROOT / "BA-Documents-Outsource" / "diagrams", ROOT / "BA-Documents-Product" / "diagrams", ROOT / "diagrams"]
        for spec in [path for folder in folders for path in sorted(folder.glob("*.json"))]:
            model = bpmn_tool.model_from_spec(json.loads(spec.read_text(encoding="utf-8")))
            waypoints = bpmn_tool.layout(model)
            shapes = [n for n in model.nodes.values() if n.category != "boundary"]
            for flow in model.flows:
                pts = waypoints[flow.id]
                for node in shapes:
                    if node.id in (flow.source, flow.target):
                        continue
                    rect = (node.x, node.y, node.w, node.h)
                    hit = any(bpmn_tool._hits_segment(rect, pts[i], pts[i + 1], pad=0) for i in range(len(pts) - 1))
                    self.assertFalse(hit, f"{spec.name}: {flow.source}->{flow.target} passes through {node.id}")

    def test_regenerate_command_stays_out_of_the_delivered_text(self):
        for doc in ROOT.glob("BA-Documents-*/*.md"):
            visible = md_to_docx.strip_html_comments(doc.read_text(encoding="utf-8"))
            self.assertNotIn("bpmn_tool.py", visible, doc.name)

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

    def test_consecutive_and_final_wide_pictures_leave_no_blank_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.png").write_bytes(wide_png(1600, 600))
            (root / "b.png").write_bytes(wide_png(1700, 600))
            (root / "cao.png").write_bytes(wide_png(1430, 1100))  # ratio 1.3: too tall for a landscape page at full width
            md = root / "doc.md"
            md.write_text("# Q\n\nMở đầu\n\n![A](a.png)\n\n![B](b.png)\n\nGiữa\n\n![Cao](cao.png)\n", encoding="utf-8")
            counts = md_to_docx.convert(md, root / "doc.docx")
            self.assertEqual(counts["landscape_pages"], 3)
            with zipfile.ZipFile(root / "doc.docx") as zf:
                document = zf.read("word/document.xml").decode("utf-8")
            # portrait end, A, B, portrait end, final section = the tall picture's landscape page
            self.assertEqual(document.count("<w:sectPr"), 5)
            self.assertNotIn("</w:sectPr></w:pPr></w:p><w:p><w:pPr><w:sectPr", document)  # no empty section
            self.assertTrue(document.rstrip().endswith('w:orient="landscape"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="709" w:footer="709" w:gutter="0"/><w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr></w:body></w:document>'))
            heights = [int(v) for v in re.findall(r'<wp:extent cx="\d+" cy="(\d+)"/>', document)]
            landscape_text_h = (11906 - 2 * 1134) * md_to_docx.EMU_PER_TWIP
            self.assertTrue(all(h <= landscape_text_h * 0.9 + 1 for h in heights), heights)

    def test_caption_under_a_wide_picture_stays_on_its_landscape_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "wf.png").write_bytes(wide_png(1600, 900))
            (root / "hep.png").write_bytes(wide_png(400, 300))
            md = root / "doc.md"
            md.write_text(
                "# SRS\n\n![SCR-01: Danh sách](wf.png)\n*Nguồn thiết kế: Figma*\n\nSau ảnh\n\n![Hẹp](hep.png)\n*Chú thích hẹp*\n",
                encoding="utf-8",
            )
            counts = md_to_docx.convert(md, root / "doc.docx")
            self.assertEqual(counts["landscape_pages"], 1)
            with zipfile.ZipFile(root / "doc.docx") as zf:
                document = zf.read("word/document.xml").decode("utf-8")
            caption_at = document.index("Nguồn thiết kế")
            paragraph = document[document.rfind("<w:p>", 0, caption_at):document.find("</w:p>", caption_at)]
            self.assertIn('w:orient="landscape"', paragraph)  # the landscape section closes on the caption
            self.assertLess(caption_at, document.index("Sau ảnh"))
            self.assertIn("Chú thích hẹp", document)
            self.assertEqual(document.count("<w:drawing>"), 2)

    def test_later_sections_continue_page_numbers(self):
        sect = '<w:sectPr><w:headerReference w:type="first" r:id="rId9"/><w:pgSz w:w="11906" w:h="16838"/><w:pgNumType w:fmt="decimal" w:start="1"/><w:titlePg/></w:sectPr>'
        later = md_to_docx.continued_section(sect)
        self.assertNotIn("titlePg", later)
        self.assertNotIn("w:start", later)
        self.assertIn('<w:pgNumType w:fmt="decimal"/>', later)


if __name__ == "__main__":
    unittest.main()
