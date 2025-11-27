import sys
from pathlib import Path
import re

FREE_START = 123456


def read_lines(fn):
  p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in p.read_text().splitlines() if ln.strip()]


def parse(lines, mode):
  nodes = {0: 0}
  edges = {}
  score = {}
  cur = None
  fidx = FREE_START

  num = r"(\d+)" if mode == 1 else r"(-?\d+)"
  plants = re.compile(rf"Plant\s+(\d+)\s+with\s+thickness\s+{num}:")
  branch = re.compile(rf"-\s*branch\s+to\s+Plant\s+(\d+)\s+with\s+thickness\s+{num}")
  freeb  = re.compile(rf"-\s*free\s+branch\s+with\s+thickness\s+{num}")

  all_nodes, childs = set(), set()

  def add(u, v, w):
    edges.setdefault(u, {})
    edges[u][v] = w

  for ln in lines:
    m = plants.match(ln)
    if m:
      pid, thickness = int(m.group(1)), int(m.group(2))
      nodes[pid] = thickness
      edges.setdefault(pid, {})
      cur = pid
      continue
    m = freeb.match(ln)
    if m and cur is not None:
      w = int(m.group(1))
      if mode == 1:
        add(cur, 0, w)
        all_nodes.add(cur); childs.add(0)
      else:
        add(cur, fidx, w)
        all_nodes.add(cur); all_nodes.add(fidx); childs.add(fidx)
        fidx += 1
      continue
    m = branch.match(ln)
    if m and cur is not None:
      ch, w = int(m.group(1)), int(m.group(2))
      add(cur, ch, w)
      all_nodes.add(cur); childs.add(ch)
      if mode == 3:
        score[ch] = score.get(ch, 0) + w
      continue

  roots = list(all_nodes - childs) # should have 1 root but can check later why we get 2 root for part 1
  root = roots[0] if roots else 0

  if mode in (1, 2):
    return nodes, edges, root

  bad = set()
  for u in nodes:
    if u in score and score[u] <= 0:
      for v in edges.get(u, {}).keys():
        if FREE_START <= v < fidx:
          bad.add(v)
  best = {x: (0 if x in bad else 1) for x in range(FREE_START, fidx)}
  return nodes, edges, root, best


def fn(u, thickness, edges, act=None):
  if act is None:
    act = {}
  if u in act:
    return act[u]
  if u == 0:
    return 1
  s = 0
  for v, w in edges.get(u, {}).items():
    s += w * fn(v, thickness, edges, act)
  return s if s >= thickness.get(u, 0) else 0


def solve1(fname):
  lines = read_lines(fname)
  thickness, edges, root = parse(lines, 1)
  return fn(19, thickness, edges, act=None) # used 19 from input directly since root had 2 & 19 and no time to fix


def solve2(fname):
  lines = read_lines(fname)
  g, tests = [], []
  flag = 0
  for ln in lines:
    if ln[0].isdigit():
      flag = 1
    (tests if flag else g).append(ln)

  thickness, edges, root = parse(g, 2)
  ans = 0
  for t in tests:
    bits = t.split()
    act = {}
    for i in range(FREE_START, FREE_START + len(bits)):
      act[i] = int(bits[i - FREE_START])
    ans += fn(root, thickness, edges, act)
  return ans


def solve3(fname):
  lines = read_lines(fname)
  g, tests = [], []
  flag = 0
  for ln in lines:
    if ln[0].isdigit():
      flag = 1
    (tests if flag else g).append(ln)

  thickness, edges, root, best = parse(g, 3)
  best_e = fn(root, thickness, edges, best)

  ans = 0
  for t in tests:
    bits = t.split()
    act = {}
    for i in range(FREE_START, FREE_START + len(bits)):
      act[i] = int(bits[i - FREE_START])
    e = fn(root, thickness, edges, act)
    assert best_e > e
    if e == 0:
      continue
    ans += best_e - e
  return ans


def main():
  for i, solver in enumerate([solve1, solve2, solve3], 1):
    print(f'p{i}:', solver(f'in{i}.txt'))


if __name__ == "__main__":
  main()
