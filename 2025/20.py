import sys
from pathlib import Path
from collections import deque
import re


def read_lines(fn):
  p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in p.read_text().splitlines() if ln.strip()]


# Used to count unique adjacent trampoline pairs (avoid double counting)
DIRS = [[-1,1],[-1,-1],[-1,0]]
def count_pairs(r, c, G):
  R,C = len(G), len(G[0])
  tot = 0
  for dr,dc in DIRS:
    nr, nc = r+dr, c+dc
    if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == 'T':
      tot += 1
  return tot


# All 6 adjacency directions in triangular grid.
BFS_DIRS = [[-1,1],[-1,-1],[1,-1],[1,1],[1,0],[-1,0]]
def bfs(sr, sc, er, ec, G, R, C):
  q = deque([(0, sr, sc)])
  vis = set()
  while q:
    cost, r, c = q.popleft()
    if (r, c) in vis:
      continue
    vis.add((r, c))
    if (r, c) == (er, ec):
      return cost
    for dr, dc in BFS_DIRS:
      nr, nc = r + dr, c + dc
      if 0 <= nr < R and 0 <= nc < C and G[nr][nc] not in ['#', '.']:
        q.append((cost + 1, nr, nc))
  return float('inf')


def modify_grid(lines):
  G = []
  for _, line in enumerate(lines):
    a,b = [], []
    fl = 1
    for i,ch in enumerate(line):
      if ch == '.':
        a.append(ch)
        b.append(ch)
      elif fl:
        a.append(ch)
        b.append('.')
        fl = 0
      elif not fl:
        a.append('.')
        b.append(ch)
        fl = 1
    G.append(a)
    G.append(b)
  return G


def solve1(fname):
  lines = read_lines(fname)
  G = modify_grid(lines)
  ans = 0
  for r in range(len(G)):
    for c in range(len(G[0])):
      if G[r][c] == 'T':
        ans += count_pairs(r, c, G)
  return ans


def solve2(fname):
  lines = read_lines(fname)
  G = modify_grid(lines)

  sr,sc,er,ec = -1,-1,-1,-1
  for r,g in enumerate(G):
    for c,ch in enumerate(g):
      if ch == 'S':
        sr, sc = r, c
      if ch == 'E':
        er, ec = r, c

  R,C = len(G), len(G[0])
  return bfs(sr,sc,er,ec,G,R,C)


def main():
  for i, solver in enumerate([solve1, solve2], 1):
    print(f'p{i}:', solver(f'in{i}.txt'))


if __name__ == "__main__":
  main()
