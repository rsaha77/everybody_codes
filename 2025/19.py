import sys
from pathlib import Path
from heapq import heappush, heappop

def read_lines(fn):
  p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in p.read_text().splitlines() if ln.strip()]


DIRS = [[-1,1], [1,1]]
def dijkstra(sr, sc, G, R, C):
  pq = []
  heappush(pq, (0, sr, sc))
  vis = set()
  while pq:
    cost, r, c = heappop(pq)
    if (r,c) in vis:
      continue
    if G[r][c] == 'E':
      return cost
    vis.add((r,c))
    for dr, dc in DIRS:
      nr, nc = r + dr, c + dc
      if 0 <= nr < R-1 and 0 <= nc < C-1 and G[nr][nc] != '#':
        new_cost = cost + 1 if nr < r else cost
        heappush(pq, (new_cost, nr, nc))
  return None


def solve1 (fname):
  lines = read_lines(fname)
  C = int(lines[-1].split(',')[0]) + 2
  R = C // 2 # adjusted with input data
  G = [list('.' * C) for _ in range(R)]
  er1, er2, ec = -1, -1, -1 # for 'E'

  for line in lines:
    wide, tall, gap = map(int,line.split(','))
    rs, re, c = R-1, R-1-tall, wide
    er1, er2, ec = re-gap, re+1, wide
    for r in range(rs, re, -1):
      G[r][c] = '#'
    for r in range(re-gap, -1, -1):
      G[r][c] = '#'

  G[R-1][0] = 'S'

  for er in range (er1, er2):
    G[er][ec] = 'E'

  return dijkstra(R-1,0,G,R,C)


def solve2 (fname):
  lines = read_lines(fname)
  C = int(lines[-1].split(',')[0]) + 2
  R = C // 3 # adjusted with input data
  G = [list('.' * C) for _ in range(R)]
  er1, er2, ec = -1, -1, -1 # for E
  done_col = set()
  for line in lines:
    wide, tall, gap = map(int,line.split(','))
    rs, re, c = R-1, R-1-tall, wide
    er1, er2, ec = re-gap, re+1, wide
    for r in range(rs, re, -1):
      if c not in done_col:
        G[r][c] = '#'
    for r in range(re, re-gap+1, -1):
      G[r][c] = '.'
    for r in range(re-gap, -1, -1):
      if c not in done_col:
        G[r][c] = '#'
    done_col.add(c)

  G[R-1][0] = 'S'

  for er in range (0, R-1):
    if G[er][ec] == '.':
      G[er][ec] = 'E'

  return dijkstra(R-1,0,G,R,C)


def main():
  for i, solver in enumerate([solve1, solve2], 1):
    print(f'p{i}:', solver(f'in{i}.txt'))


if __name__ == "__main__":
  main()
