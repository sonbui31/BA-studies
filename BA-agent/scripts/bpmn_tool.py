#!/usr/bin/env python3
"""BPMN 2.0 for BA documents: build .bpmn from a short JSON spec, check it, render it.

    python bpmn_tool.py build <spec.json> [-o out.bpmn] [--png out.png] [--browser PATH]
    python bpmn_tool.py check <file.bpmn | folder>
    python bpmn_tool.py render <file.bpmn> <out.png|out.svg> [--browser PATH]

The .bpmn output is standard BPMN 2.0 XML (ISO/IEC 19510) with diagram interchange (BPMNDI):
one pool, horizontal lanes, left-to-right layout. It opens and edits in bpmn.io / Camunda Modeler
and imports into most BPMN tools. Rendering uses bpmn-js through scripts/bpmn_render.mjs (Node).

Spec (JSON):
{
  "id": "p1_tobe", "name": "P1 To-Be: Điều chuyển tài sản", "pool": "Bệnh viện",
  "lanes": [{"id": "khoa_giao", "name": "Khoa giao"}, ...],
  "nodes": [
    {"id": "start", "type": "start", "name": "Khoa cần chuyển tài sản", "lane": "khoa_giao"},
    {"id": "t1", "type": "user", "name": "Tạo yêu cầu điều chuyển", "lane": "khoa_giao"},
    {"id": "g1", "type": "xor", "name": "Tài sản bị khóa?", "lane": "he_thong"},
    {"id": "w1", "type": "boundary_timer", "name": "48 giờ", "attached_to": "t4", "interrupting": false},
    ...
  ],
  "flows": [["start", "t1"], ["g1", "end_blocked", "Có"], {"from": "g1", "to": "t2", "name": "Không", "default": true}]
}
Node types: start, start_timer, start_message, end, end_message, task, user, service, send, receive,
manual, business_rule, subprocess, xor, and, or, timer, message_catch, message_throw, boundary_timer,
boundary_message. Optional per node: "row" (stack position inside the lane), "col" (force a column),
"highlight" ("pain" / "new"). Task kinds are drawn as plain tasks without icons unless the spec sets
"task_icons": true (the icons overlap task names in small boxes).
Exit codes: 0 ok; 1 model errors (or render failure); 2 bad arguments, unreadable file, missing Node.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.sax.saxutils import escape

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"
NS = {"bpmn": BPMN_NS, "bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI"}

# spec type -> (BPMN element, event definition or None, category)
TYPES: Dict[str, Tuple[str, Optional[str], str]] = {
    "start": ("startEvent", None, "event"),
    "start_timer": ("startEvent", "timerEventDefinition", "event"),
    "start_message": ("startEvent", "messageEventDefinition", "event"),
    "end": ("endEvent", None, "event"),
    "end_message": ("endEvent", "messageEventDefinition", "event"),
    "task": ("task", None, "activity"),
    "user": ("userTask", None, "activity"),
    "service": ("serviceTask", None, "activity"),
    "send": ("sendTask", None, "activity"),
    "receive": ("receiveTask", None, "activity"),
    "manual": ("manualTask", None, "activity"),
    "business_rule": ("businessRuleTask", None, "activity"),
    "subprocess": ("subProcess", None, "activity"),
    "xor": ("exclusiveGateway", None, "gateway"),
    "and": ("parallelGateway", None, "gateway"),
    "or": ("inclusiveGateway", None, "gateway"),
    "timer": ("intermediateCatchEvent", "timerEventDefinition", "event"),
    "message_catch": ("intermediateCatchEvent", "messageEventDefinition", "event"),
    "message_throw": ("intermediateThrowEvent", "messageEventDefinition", "event"),
    "boundary_timer": ("boundaryEvent", "timerEventDefinition", "boundary"),
    "boundary_message": ("boundaryEvent", "messageEventDefinition", "boundary"),
}
ELEMENT_KIND = {element: (category, spec) for spec, (element, _, category) in TYPES.items()}
ACTIVITIES = {"task", "userTask", "serviceTask", "sendTask", "receiveTask", "manualTask", "businessRuleTask", "scriptTask", "subProcess", "callActivity"}

# Optional colouring (bpmn.io colour extension, read by bpmn.io and Camunda Modeler):
# pain = step causing a pain point in an As-Is model, new = step introduced by the To-Be model.
HIGHLIGHTS = {"pain": ("#C53030", "#FFF5F5"), "new": ("#2F855A", "#F0FFF4")}
SIZE = {"activity": (130, 80), "gateway": (50, 50), "event": (36, 36), "boundary": (36, 36)}
COL_GAP, MIN_COL_W, ROW_H = 60, 110, 130
POOL_X, POOL_Y, POOL_LABEL, LANE_LABEL = 160, 80, 30, 30
LANE_PAD = 35


@dataclass
class Node:
    id: str
    element: str
    category: str
    name: str = ""
    lane: Optional[str] = None
    event_def: Optional[str] = None
    attached_to: Optional[str] = None
    interrupting: bool = True
    row: Optional[int] = None
    col: Optional[int] = None
    highlight: Optional[str] = None
    # layout
    x: float = 0
    y: float = 0
    w: float = 0
    h: float = 0


@dataclass
class Flow:
    id: str
    source: str
    target: str
    name: str = ""
    default: bool = False


@dataclass
class Model:
    id: str
    name: str
    pool: str
    lanes: List[Tuple[str, str]] = field(default_factory=list)
    nodes: Dict[str, Node] = field(default_factory=dict)
    flows: List[Flow] = field(default_factory=list)
    # Task type icons (person, gear, envelope...) sit in the top-left corner and overlap the
    # task name in small boxes. Off by default: tasks are drawn as plain BPMN tasks.
    task_icons: bool = False


# ---------------------------------------------------------------- spec / file loading


def _slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", value)


def model_from_spec(spec: dict) -> Model:
    model = Model(id=_slug(spec.get("id", "process")), name=spec.get("name", ""), pool=spec.get("pool", spec.get("name", "")))
    model.task_icons = bool(spec.get("task_icons", False))
    model.lanes = [(_slug(lane["id"]), lane.get("name", lane["id"])) for lane in spec.get("lanes", [])]
    for raw in spec.get("nodes", []):
        kind = raw.get("type", "task")
        if kind not in TYPES:
            raise ValueError(f"node {raw.get('id')}: unknown type '{kind}' (use one of {', '.join(TYPES)})")
        element, event_def, category = TYPES[kind]
        node = Node(
            id=_slug(raw["id"]),
            element=element,
            category=category,
            name=raw.get("name", ""),
            lane=_slug(raw["lane"]) if raw.get("lane") else None,
            event_def=event_def,
            attached_to=_slug(raw["attached_to"]) if raw.get("attached_to") else None,
            interrupting=bool(raw.get("interrupting", True)),
            row=raw.get("row"),
            col=raw.get("col"),
            highlight=raw.get("highlight"),
        )
        if node.id in model.nodes:
            raise ValueError(f"duplicate node id {node.id}")
        model.nodes[node.id] = node
    for index, raw in enumerate(spec.get("flows", []), start=1):
        if isinstance(raw, (list, tuple)):
            source, target, name = raw[0], raw[1], (raw[2] if len(raw) > 2 else "")
            default = False
        else:
            source, target, name, default = raw["from"], raw["to"], raw.get("name", ""), bool(raw.get("default"))
        model.flows.append(Flow(id=f"Flow_{index}", source=_slug(source), target=_slug(target), name=name, default=default))
    for node in model.nodes.values():
        if node.category == "boundary" and node.attached_to in model.nodes and not node.lane:
            node.lane = model.nodes[node.attached_to].lane
    return model


def model_from_bpmn(path: Path) -> Model:
    root = ET.parse(path).getroot()
    process = root.find("bpmn:process", NS)
    if process is None:
        raise ValueError("no <process> element")
    participant = root.find(".//bpmn:participant", NS)
    model = Model(id=process.get("id", "process"), name=process.get("name", ""), pool=participant.get("name", "") if participant is not None else "")
    lane_of: Dict[str, str] = {}
    for lane in process.iter(f"{{{BPMN_NS}}}lane"):
        model.lanes.append((lane.get("id"), lane.get("name", "")))
        for ref in lane.findall("bpmn:flowNodeRef", NS):
            lane_of[(ref.text or "").strip()] = lane.get("id")
    defaults = {}
    for child in process:
        tag = child.tag.split("}")[1]
        if tag in ELEMENT_KIND:
            category, _ = ELEMENT_KIND[tag]
            event_def = None
            for definition in ("timerEventDefinition", "messageEventDefinition", "errorEventDefinition", "signalEventDefinition"):
                if child.find(f"bpmn:{definition}", NS) is not None:
                    event_def = definition
            model.nodes[child.get("id")] = Node(
                id=child.get("id"),
                element=tag,
                category=category,
                name=child.get("name", ""),
                lane=lane_of.get(child.get("id")),
                event_def=event_def,
                attached_to=child.get("attachedToRef"),
                interrupting=child.get("cancelActivity", "true") != "false",
            )
            if child.get("default"):
                defaults[child.get("default")] = True
        elif tag in ("scriptTask", "callActivity"):
            model.nodes[child.get("id")] = Node(id=child.get("id"), element=tag, category="activity", name=child.get("name", ""), lane=lane_of.get(child.get("id")))
    for child in process.findall("bpmn:sequenceFlow", NS):
        model.flows.append(
            Flow(id=child.get("id"), source=child.get("sourceRef"), target=child.get("targetRef"), name=child.get("name", ""), default=child.get("id") in defaults)
        )
    return model


# ---------------------------------------------------------------- validation


def validate(model: Model) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    nodes = model.nodes
    lane_ids = {lane_id for lane_id, _ in model.lanes}
    incoming: Dict[str, List[Flow]] = {node_id: [] for node_id in nodes}
    outgoing: Dict[str, List[Flow]] = {node_id: [] for node_id in nodes}
    for flow in model.flows:
        if flow.source not in nodes or flow.target not in nodes:
            errors.append(f"{flow.id}: luồng trỏ tới phần tử không tồn tại ({flow.source} -> {flow.target})")
            continue
        outgoing[flow.source].append(flow)
        incoming[flow.target].append(flow)

    starts = [n for n in nodes.values() if n.element == "startEvent"]
    if not starts:
        errors.append("không có sự kiện bắt đầu (startEvent)")
    if not any(n.element == "endEvent" for n in nodes.values()):
        errors.append("không có sự kiện kết thúc (endEvent)")

    for node in nodes.values():
        label = f"{node.id} \"{node.name}\""
        if model.lanes and node.lane not in lane_ids:
            errors.append(f"{label}: không thuộc lane nào")
        if not node.name.strip() and node.category != "gateway":
            warnings.append(f"{node.id}: chưa đặt tên")
        if node.element == "startEvent" and incoming[node.id]:
            errors.append(f"{label}: sự kiện bắt đầu không được có luồng vào")
        if node.element == "endEvent" and outgoing[node.id]:
            errors.append(f"{label}: sự kiện kết thúc không được có luồng ra")
        if node.element not in ("startEvent", "boundaryEvent") and not incoming[node.id]:
            errors.append(f"{label}: không có luồng vào (phần tử lơ lửng)")
        if node.element != "endEvent" and not outgoing[node.id]:
            errors.append(f"{label}: không có luồng ra (luồng bị cụt; kết thúc bằng endEvent)")
        if node.element == "boundaryEvent":
            host = nodes.get(node.attached_to or "")
            if not host or host.element not in ACTIVITIES:
                errors.append(f"{label}: sự kiện biên phải gắn vào một task (attached_to)")
        if node.category == "gateway":
            outs, ins = outgoing[node.id], incoming[node.id]
            if node.element in ("exclusiveGateway", "inclusiveGateway") and len(outs) >= 2:
                for flow in outs:
                    if not flow.name.strip() and not flow.default:
                        errors.append(f"{label}: nhánh {flow.source} -> {flow.target} thiếu điều kiện")
                if node.element == "exclusiveGateway" and not node.name.strip().endswith("?"):
                    warnings.append(f"{label}: cổng loại trừ nên đặt tên là một câu hỏi (kết thúc bằng \"?\")")
            if len(outs) < 2 and len(ins) < 2:
                warnings.append(f"{label}: cổng chỉ có một luồng vào và một luồng ra, không cần thiết")

    split = sum(1 for n in nodes.values() if n.element == "parallelGateway" and len(outgoing[n.id]) >= 2)
    join = sum(1 for n in nodes.values() if n.element == "parallelGateway" and len(incoming[n.id]) >= 2)
    if split != join:
        warnings.append(f"cổng song song: {split} điểm tách nhưng {join} điểm hợp")

    reached = set()
    stack = [n.id for n in starts]
    while stack:
        current = stack.pop()
        if current in reached:
            continue
        reached.add(current)
        stack.extend(flow.target for flow in outgoing.get(current, []))
        stack.extend(n.id for n in nodes.values() if n.attached_to == current)
    for node in nodes.values():
        if node.id not in reached and starts:
            errors.append(f"{node.id} \"{node.name}\": không đi tới được từ sự kiện bắt đầu")
    return errors, warnings


# ---------------------------------------------------------------- layout


def layout(model: Model) -> Dict[str, List[Tuple[float, float]]]:
    nodes, flows = model.nodes, [f for f in model.flows if f.source in model.nodes and f.target in model.nodes]
    succ: Dict[str, List[str]] = {n: [] for n in nodes}
    for flow in flows:
        succ[flow.source].append(flow.target)
    for node in nodes.values():  # a boundary event leaves from its host
        if node.category == "boundary" and node.attached_to in nodes:
            succ[node.attached_to].append(node.id)

    # Back edges via DFS from the starts (order of declaration).
    back = set()
    state: Dict[str, int] = {}

    def dfs(node_id: str) -> None:
        state[node_id] = 1
        for nxt in succ[node_id]:
            if state.get(nxt) == 1:
                back.add((node_id, nxt))
            elif nxt not in state:
                dfs(nxt)
        state[node_id] = 2

    for node in nodes.values():
        if node.element == "startEvent" and node.id not in state:
            dfs(node.id)
    for node_id in nodes:
        if node_id not in state:
            dfs(node_id)

    # Longest-path columns on the DAG; a boundary event sits in its host's column.
    col: Dict[str, int] = {}
    order: List[str] = []
    indegree = {n: 0 for n in nodes}
    for source, targets in succ.items():
        for target in targets:
            if (source, target) not in back:
                indegree[target] += 1
    ready = [n for n in nodes if indegree[n] == 0]
    while ready:
        current = ready.pop(0)
        order.append(current)
        for target in succ[current]:
            if (current, target) in back:
                continue
            step = 0 if nodes[target].category == "boundary" else 1
            col[target] = max(col.get(target, 0), col.get(current, 0) + step)
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    for node in nodes.values():
        col.setdefault(node.id, 0)
        if node.col is not None:
            col[node.id] = node.col
        node.col = col[node.id]

    lane_ids = [lane_id for lane_id, _ in model.lanes] or [None]
    rows_in_lane: Dict[Optional[str], int] = {lane: 1 for lane in lane_ids}
    taken: Dict[Tuple[Optional[str], int, int], str] = {}
    for node_id in order + [n for n in nodes if n not in order]:
        node = nodes[node_id]
        if node.category == "boundary":
            continue
        row = node.row if node.row is not None else 0
        while node.row is None and (node.lane, node.col, row) in taken:
            row += 1
        node.row = row
        taken[(node.lane, node.col, row)] = node.id
        rows_in_lane[node.lane] = max(rows_in_lane.get(node.lane, 1), row + 1)

    columns = max((n.col for n in nodes.values()), default=0) + 1
    content_x = POOL_X + POOL_LABEL + LANE_LABEL + 30
    # Column width follows its widest element: a column of events or gateways stays narrow.
    col_width = [MIN_COL_W] * columns
    for node in nodes.values():
        if node.category != "boundary":
            col_width[node.col] = max(col_width[node.col], SIZE[node.category][0] + COL_GAP)
    for flow in flows:
        source, target = nodes[flow.source], nodes[flow.target]
        if flow.name and source.category == "gateway" and target.col == source.col + 1 and source.row == target.row and source.lane == target.lane:
            gap_needed = flow_label_width(flow.name) + 16
            gap_now = (col_width[source.col] - source.w) / 2 + (col_width[target.col] - SIZE[target.category][0]) / 2
            if gap_now < gap_needed:
                col_width[source.col] += 2 * (gap_needed - gap_now)
    col_left = [content_x + sum(col_width[:index]) for index in range(columns)]
    lane_top: Dict[Optional[str], float] = {}
    y = POOL_Y
    for lane in lane_ids:
        lane_top[lane] = y
        y += rows_in_lane.get(lane, 1) * ROW_H + 2 * LANE_PAD
    model_height = y - POOL_Y
    model_width = content_x - POOL_X + sum(col_width) + 20

    for node in nodes.values():
        node.w, node.h = SIZE[node.category]
        if node.category == "boundary":
            continue
        cx = col_left[node.col] + col_width[node.col] / 2
        cy = lane_top[node.lane] + LANE_PAD + node.row * ROW_H + ROW_H / 2
        node.x, node.y = cx - node.w / 2, cy - node.h / 2
    for node in nodes.values():
        if node.category == "boundary":
            host = nodes[node.attached_to]
            node.x = host.x + host.w * 0.7 - node.w / 2
            node.y = host.y + host.h - node.h / 2

    model._geometry = {  # type: ignore[attr-defined]
        "pool": (POOL_X, POOL_Y, model_width, model_height),
        "lanes": {lane: (POOL_X + POOL_LABEL, lane_top[lane], model_width - POOL_LABEL, rows_in_lane.get(lane, 1) * ROW_H + 2 * LANE_PAD) for lane in lane_ids},
    }

    def center(n: Node) -> Tuple[float, float]:
        return n.x + n.w / 2, n.y + n.h / 2

    # Routing rules (what a BA would draw by hand):
    # - vertical segments run in the gap left of the target column, where no element sits;
    # - a gateway leaves from its top/bottom only when its own column is free in that direction,
    #   and only one flow per direction (a loop-back flow takes the bottom);
    # - a flow merging into a gateway from another row enters it from the top or bottom.
    def is_back(flow: Flow) -> bool:
        return (flow.source, flow.target) in back or nodes[flow.target].col <= nodes[flow.source].col

    def cy(n: Node) -> float:
        return n.y + n.h / 2

    branches_down = {
        flow.source for flow in flows
        if nodes[flow.source].category == "gateway" and not is_back(flow) and cy(nodes[flow.target]) > cy(nodes[flow.source]) + 1
    }
    loop_over_top = {flow.id for flow in flows if is_back(flow) and flow.source in branches_down}
    loops_from = {flow.source for flow in flows if is_back(flow) and flow.id not in loop_over_top}
    placed = [n for n in nodes.values() if n.category != "boundary"]

    def clear(column: int, y1: float, y2: float, skip: Tuple[str, ...]) -> bool:
        low, high = min(y1, y2), max(y1, y2)
        return not any(n.col == column and n.id not in skip and low < n.y + n.h / 2 < high for n in placed)

    used_exit: Dict[Tuple[str, str], bool] = {}
    for node_id in loops_from:
        used_exit[(node_id, "down")] = True
    for flow in flows:
        if flow.id in loop_over_top:
            used_exit[(flow.source, "up")] = True

    # (c) flows entering a gateway take their side first, so the exits avoid it.
    flows = sorted(flows, key=lambda f: 0 if nodes[f.target].category == "gateway" else 1)

    waypoints: Dict[str, List[Tuple[float, float]]] = {}
    for flow in flows:
        s, t = nodes[flow.source], nodes[flow.target]
        sx, sy = center(s)
        tx, ty = center(t)
        gap_x = t.x - (col_width[t.col] - t.w) / 2 - COL_GAP / 4 if t.category != "boundary" else t.x - 20
        direction = "down" if ty > sy else "up"
        if s.category == "boundary":
            if t.x <= sx:
                pts = [(sx, s.y + s.h), (sx, t.y + t.h + 20), (tx, t.y + t.h + 20), (tx, t.y + t.h)]
            elif abs(ty - sy) > 1:
                pts = [(sx, s.y + s.h), (sx, ty), (t.x, ty)]
            else:
                pts = [(sx, s.y + s.h), (sx, ty + 40), (t.x, ty + 40)]
        elif flow.id in loop_over_top:
            above = min(s.y, t.y) - 22
            pts = [(sx, s.y), (sx, above), (tx, above), (tx, t.y)]
        elif (flow.source, flow.target) in back or t.col <= s.col:
            below = max(s.y + s.h, t.y + t.h) + 22
            pts = [(sx, s.y + s.h), (sx, below), (tx, below), (tx, t.y + t.h)]
        elif abs(ty - sy) < 1:
            pts = [(s.x + s.w, sy), (t.x, ty)]
        elif t.category == "gateway" and clear(t.col, sy, ty, (s.id, t.id)):
            pts = [(s.x + s.w, sy), (tx, sy), (tx, t.y + t.h if sy > ty else t.y)]
            used_exit[(t.id, "down" if sy > ty else "up")] = True
        elif (
            s.category == "gateway"
            and not used_exit.get((s.id, direction))
            and clear(s.col, sy, ty, (s.id, t.id))
        ):
            used_exit[(s.id, direction)] = True
            pts = [(sx, s.y + s.h if direction == "down" else s.y), (sx, ty), (t.x, ty)]
        else:
            pts = [(s.x + s.w, sy), (gap_x, sy), (gap_x, ty), (t.x, ty)]
        waypoints[flow.id] = pts
    return waypoints


# ---------------------------------------------------------------- XML

LABEL_W, LABEL_H = 110, 40


def flow_label_width(name: str) -> int:
    return min(130, max(24, int(len(name) * 7.2) + 8))


Rect = Tuple[float, float, float, float]


def _overlaps(a: Rect, b: Rect) -> bool:
    return a[0] < b[0] + b[2] and b[0] < a[0] + a[2] and a[1] < b[1] + b[3] and b[1] < a[1] + a[3]


def _hits_segment(rect: Rect, p: Tuple[float, float], q: Tuple[float, float], pad: float = 2) -> bool:
    x, y, w, h = rect[0] - pad, rect[1] - pad, rect[2] + 2 * pad, rect[3] + 2 * pad
    (x1, y1), (x2, y2) = p, q
    if abs(y1 - y2) < 1:  # horizontal
        return y <= y1 <= y + h and min(x1, x2) < x + w and max(x1, x2) > x
    return x <= x1 <= x + w and min(y1, y2) < y + h and max(y1, y2) > y


def place_labels(model: Model, waypoints: Dict[str, List[Tuple[float, float]]]) -> Tuple[Dict[str, Rect], Dict[str, Rect]]:
    """Put every label on the first candidate spot that touches no shape, no flow and no other label."""
    nodes = model.nodes
    shapes: Dict[str, Rect] = {n.id: (n.x, n.y, n.w, n.h) for n in nodes.values()}
    segments = [(fid, pts[i], pts[i + 1]) for fid, pts in waypoints.items() for i in range(len(pts) - 1)]
    # Lane and pool borders are obstacles too: a label must not straddle two lanes.
    geo = getattr(model, "_geometry", None)
    if geo:
        for lx, ly, lw, lh in list(geo["lanes"].values()) + [geo["pool"]]:
            segments += [("_border", (lx, ly), (lx + lw, ly)), ("_border", (lx, ly + lh), (lx + lw, ly + lh))]
    taken: List[Rect] = []

    def collisions(rect: Rect, own_flow: Optional[str] = None) -> int:
        count = sum(1 for shape in shapes.values() if _overlaps(rect, shape)) * 3
        count += sum(1 for other in taken if _overlaps(rect, other)) * 3
        # A label may sit right next to its own flow, never across it.
        count += sum(1 for fid, p, q in segments if _hits_segment(rect, p, q, pad=0 if fid == own_flow else 2))
        return count

    def choose(candidates: List[Rect], own_flow: Optional[str] = None) -> Rect:
        # First spot with no collision; otherwise the least bad one (labels over labels or shapes worst).
        scored = [(collisions(c, own_flow), index, c) for index, c in enumerate(candidates)]
        rect = min(scored)[2]
        taken.append(rect)
        return rect

    node_labels: Dict[str, Rect] = {}
    for node in nodes.values():
        if node.category not in ("event", "gateway", "boundary") or not node.name:
            continue
        w, h = LABEL_W, LABEL_H
        cx = node.x + node.w / 2
        top, bottom, left, right = node.y, node.y + node.h, node.x, node.x + node.w
        candidates = [
            (cx - w / 2, bottom + 4, w, h),
            (cx - w / 2, top - h - 4, w, h),
            (left - w + 4, top - h - 2, w, h),
            (left - w + 4, bottom + 2, w, h),
            (right - 4, top - h - 2, w, h),
            (right - 4, bottom + 2, w, h),
            (left - w - 4, node.y + node.h / 2 - h / 2, w, h),
        ]
        if node.category == "boundary":
            candidates = [(left - w - 2, node.y + node.h / 2, w, h), (right + 2, node.y + node.h / 2, w, h)] + candidates
        node_labels[node.id] = choose(candidates)

    flow_labels: Dict[str, Rect] = {}
    for flow in model.flows:
        pts = waypoints.get(flow.id)
        if not flow.name or not pts:
            continue
        w = flow_label_width(flow.name)
        lines = max(1, -(-int(len(flow.name) * 7.2) // max(w - 8, 1)))
        h = 16 * lines + 2
        candidates: List[Rect] = []
        for (x1, y1), (x2, y2) in ([(pts[0], pts[1])] + ([(pts[-2], pts[-1])] if len(pts) > 2 else [])):
            if abs(y1 - y2) < 1:  # horizontal segment: above or below, near its start or its end
                lo, hi = min(x1, x2), max(x1, x2)
                candidates += [(lo + 4, y1 - h - 2, w, h), (lo + 4, y1 + 3, w, h), (hi - w - 4, y1 - h - 2, w, h), (hi - w - 4, y1 + 3, w, h)]
            else:  # vertical segment: right or left of it, near its start
                ys = y1 + 4 if y2 > y1 else y1 - h - 4
                candidates += [(x1 + 6, ys, w, h), (x1 - w - 6, ys, w, h)]
        mid = max(range(len(pts) - 1), key=lambda i: abs(pts[i + 1][0] - pts[i][0]) + abs(pts[i + 1][1] - pts[i][1]))
        (mx1, my1), (mx2, my2) = pts[mid], pts[mid + 1]
        candidates.append(((mx1 + mx2) / 2 - w / 2, (my1 + my2) / 2 - h - 2, w, h))
        flow_labels[flow.id] = choose(candidates, own_flow=flow.id)
    return node_labels, flow_labels


def to_xml(model: Model) -> str:
    waypoints = layout(model)
    node_labels, flow_labels = place_labels(model, waypoints)
    geo = model._geometry  # type: ignore[attr-defined]
    nodes = model.nodes
    process_id = f"Process_{model.id}"
    out: List[str] = ['<?xml version="1.0" encoding="UTF-8"?>']
    out.append(
        '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
        'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
        'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:bioc="http://bpmn.io/schema/bpmn/biocolor/1.0" '
        'xmlns:color="http://www.omg.org/spec/BPMN/non-normative/color/1.0" '
        f'id="Definitions_{model.id}" targetNamespace="http://bpmn.io/schema/bpmn" exporter="BA-agent bpmn_tool.py" exporterVersion="1.0">'
    )
    out.append(f'  <bpmn:collaboration id="Collaboration_{model.id}">')
    out.append(f'    <bpmn:participant id="Participant_{model.id}" name="{escape(model.pool, {chr(34): "&quot;"})}" processRef="{process_id}" />')
    out.append("  </bpmn:collaboration>")
    out.append(f'  <bpmn:process id="{process_id}" name="{escape(model.name, {chr(34): "&quot;"})}" isExecutable="false">')
    if model.lanes:
        out.append(f'    <bpmn:laneSet id="LaneSet_{model.id}">')
        for lane_id, lane_name in model.lanes:
            out.append(f'      <bpmn:lane id="{lane_id}" name="{escape(lane_name, {chr(34): "&quot;"})}">')
            for node in nodes.values():
                if node.lane == lane_id:
                    out.append(f"        <bpmn:flowNodeRef>{node.id}</bpmn:flowNodeRef>")
            out.append("      </bpmn:lane>")
        out.append("    </bpmn:laneSet>")
    flows_out: Dict[str, List[str]] = {n: [] for n in nodes}
    flows_in: Dict[str, List[str]] = {n: [] for n in nodes}
    for flow in model.flows:
        flows_out[flow.source].append(flow.id)
        flows_in[flow.target].append(flow.id)
    for node in nodes.values():
        attrs = f'id="{node.id}" name="{escape(node.name, {chr(34): "&quot;"})}"'
        if node.element == "boundaryEvent":
            attrs += f' attachedToRef="{node.attached_to}"'
            if not node.interrupting:
                attrs += ' cancelActivity="false"'
        if node.category == "gateway":
            default = next((f.id for f in model.flows if f.source == node.id and f.default), None)
            if default:
                attrs += f' default="{default}"'
        element = node.element
        if not model.task_icons and node.category == "activity" and element != "subProcess":
            element = "task"
        out.append(f"    <bpmn:{element} {attrs}>")
        out.extend(f"      <bpmn:incoming>{fid}</bpmn:incoming>" for fid in flows_in[node.id])
        out.extend(f"      <bpmn:outgoing>{fid}</bpmn:outgoing>" for fid in flows_out[node.id])
        if node.event_def:
            out.append(f'      <bpmn:{node.event_def} id="{node.id}_def" />')
        out.append(f"    </bpmn:{element}>")
    for flow in model.flows:
        name = f' name="{escape(flow.name, {chr(34): "&quot;"})}"' if flow.name else ""
        out.append(f'    <bpmn:sequenceFlow id="{flow.id}"{name} sourceRef="{flow.source}" targetRef="{flow.target}" />')
    out.append("  </bpmn:process>")

    out.append(f'  <bpmndi:BPMNDiagram id="BPMNDiagram_{model.id}">')
    out.append(f'    <bpmndi:BPMNPlane id="BPMNPlane_{model.id}" bpmnElement="Collaboration_{model.id}">')
    px, py, pw, ph = geo["pool"]
    out.append(f'      <bpmndi:BPMNShape id="Participant_{model.id}_di" bpmnElement="Participant_{model.id}" isHorizontal="true">')
    out.append(f'        <dc:Bounds x="{px:.0f}" y="{py:.0f}" width="{pw:.0f}" height="{ph:.0f}" />')
    out.append("      </bpmndi:BPMNShape>")
    for lane_id, _ in model.lanes:
        lx, ly, lw, lh = geo["lanes"][lane_id]
        out.append(f'      <bpmndi:BPMNShape id="{lane_id}_di" bpmnElement="{lane_id}" isHorizontal="true">')
        out.append(f'        <dc:Bounds x="{lx:.0f}" y="{ly:.0f}" width="{lw:.0f}" height="{lh:.0f}" />')
        out.append("      </bpmndi:BPMNShape>")
    for node in nodes.values():
        extra = ' isMarkerVisible="true"' if node.element == "exclusiveGateway" else ""
        if node.highlight in HIGHLIGHTS:
            stroke, fill = HIGHLIGHTS[node.highlight]
            extra += f' bioc:stroke="{stroke}" bioc:fill="{fill}" color:border-color="{stroke}" color:background-color="{fill}"'
        out.append(f'      <bpmndi:BPMNShape id="{node.id}_di" bpmnElement="{node.id}"{extra}>')
        out.append(f'        <dc:Bounds x="{node.x:.0f}" y="{node.y:.0f}" width="{node.w:.0f}" height="{node.h:.0f}" />')
        if node.category in ("event", "gateway", "boundary") and node.name:
            lx, ly, lw, lh = node_labels[node.id]
            out.append("        <bpmndi:BPMNLabel>")
            out.append(f'          <dc:Bounds x="{lx:.0f}" y="{ly:.0f}" width="{lw:.0f}" height="{lh:.0f}" />')
            out.append("        </bpmndi:BPMNLabel>")
        out.append("      </bpmndi:BPMNShape>")
    for flow in model.flows:
        pts = waypoints.get(flow.id)
        if not pts:
            continue
        out.append(f'      <bpmndi:BPMNEdge id="{flow.id}_di" bpmnElement="{flow.id}">')
        out.extend(f'        <di:waypoint x="{x:.0f}" y="{y:.0f}" />' for x, y in pts)
        if flow.id in flow_labels:
            lx, ly, lw, lh = flow_labels[flow.id]
            out.append(f'        <bpmndi:BPMNLabel><dc:Bounds x="{lx:.0f}" y="{ly:.0f}" width="{lw:.0f}" height="{lh:.0f}" /></bpmndi:BPMNLabel>')
        out.append("      </bpmndi:BPMNEdge>")
    out.append("    </bpmndi:BPMNPlane>")
    out.append("  </bpmndi:BPMNDiagram>")
    out.append("</bpmn:definitions>")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- rendering


def render(bpmn_path: Path, out_path: Path, browser: Optional[str] = None) -> Tuple[int, str]:
    node = shutil.which("node")
    script = Path(__file__).resolve().parent / "bpmn_render.mjs"
    if not node:
        return 2, "cần Node.js để vẽ ảnh (bpmn_render.mjs)"
    cmd = [node, str(script), str(bpmn_path), str(out_path)]
    if browser:
        cmd += ["--browser", browser]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def report(name: str, errors: List[str], warnings: List[str]) -> None:
    status = "LỖI" if errors else ("CẢNH BÁO" if warnings else "ĐẠT")
    print(f"## {name}: {status}")
    for item in errors:
        print(f"- LỖI: {item}")
    for item in warnings:
        print(f"- Cảnh báo: {item}")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Sinh, kiểm tra và vẽ sơ đồ BPMN 2.0 (.bpmn) cho tài liệu BA.")
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build", help="Sinh .bpmn từ spec JSON")
    build.add_argument("spec", type=Path)
    build.add_argument("-o", "--output", type=Path, default=None, help="File .bpmn (mặc định: cạnh spec, cùng tên)")
    build.add_argument("--png", type=Path, default=None, help="Vẽ thêm ảnh PNG (cần Node.js + bpmn-js)")
    build.add_argument("--svg", type=Path, default=None, help="Vẽ thêm ảnh SVG")
    build.add_argument("--browser", default=os.environ.get("BA_MERMAID_BROWSER"))
    check = sub.add_parser("check", help="Kiểm tra file .bpmn hoặc mọi .bpmn trong thư mục")
    check.add_argument("target", type=Path)
    check.add_argument("--strict", action="store_true", help="Cảnh báo cũng làm mã thoát 1")
    rend = sub.add_parser("render", help="Vẽ .bpmn thành PNG/SVG")
    rend.add_argument("bpmn", type=Path)
    rend.add_argument("output", type=Path)
    rend.add_argument("--browser", default=os.environ.get("BA_MERMAID_BROWSER"))
    args = parser.parse_args(argv)

    if args.command == "build":
        try:
            model = model_from_spec(json.loads(args.spec.read_text(encoding="utf-8")))
        except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
            print(f"LỖI: không đọc được spec {args.spec}: {exc}")
            return 2
        errors, warnings = validate(model)
        report(str(args.spec), errors, warnings)
        if errors:
            print("Không ghi file .bpmn vì mô hình còn lỗi.")
            return 1
        output = args.output or args.spec.with_suffix(".bpmn")
        output.write_text(to_xml(model), encoding="utf-8")
        print(f"OK: {output}")
        for image in (args.png, args.svg):
            if image:
                code, message = render(output, image, args.browser)
                print(message)
                if code:
                    return code
        return 0

    if args.command == "check":
        if not args.target.exists():
            print(f"LỖI: không tìm thấy {args.target}")
            return 2
        files = [args.target] if args.target.is_file() else sorted(args.target.rglob("*.bpmn"))
        failed = False
        for path in files:
            try:
                errors, warnings = validate(model_from_bpmn(path))
            except (ET.ParseError, ValueError) as exc:
                errors, warnings = [f"không đọc được XML: {exc}"], []
            report(str(path), errors, warnings)
            failed = failed or bool(errors) or (args.strict and bool(warnings))
        print(f"\n{len(files)} file .bpmn")
        return 1 if failed else 0

    code, message = render(args.bpmn, args.output, args.browser)
    print(message)
    return code


if __name__ == "__main__":
    sys.exit(main())
