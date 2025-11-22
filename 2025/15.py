import sys
from collections import deque
from pathlib import Path


def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]

HV_DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]

dir_map = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1)
}

turns = {
  'R': {'>': 'v', 'v': '<', '<': '^', '^': '>'},
  'L': {'v': '>', '>': '^', '^': '<', '<': 'v'}
}

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
    for dr, dc in HV_DIR:
      nr, nc = r + dr, c + dc
      if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#':
        q.append((cost + 1, nr, nc))
  return float('inf')


def move(curr_drc, r,c,R,C,G,drc,ln):
  new_drc = turns[drc][curr_drc]
  dr, dc = dir_map[new_drc]
  for _ in range(ln):
    r += dr
    c += dc
    G[r][c] = '#'
  return new_drc, r, c


def solve1(fname, N=100):
  L = list(read_lines(fname)[0].split(','))
  R = C = N
  G = [list('.' * C) for _ in range(R)]
  sr = sc = N // 2
  G[sr][sc] = 'S'
  curr_drc = '^'
  r, c = sr, sc
  for x in L:
    drc, ln = x[0], int(x[1:])
    curr_drc, r, c = move(curr_drc, r,c,R,C,G,drc,ln)
  G[r][c] = 'E'

  return bfs(sr, sc, r, c, G, R, C) # same cost of each path, no need dijkstra


def solve2(fname):
  return solve1(fname,N=1000)


def main():
  for i, fn_solver in enumerate([solve1, solve2], 1):
    print(f'p{i}:', fn_solver(f'in{i}.txt'))


if __name__ == '__main__':
  main()
