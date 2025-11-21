import sys
import time
from copy import deepcopy
from pathlib import Path


def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]


DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

def dfs(r, c, R, C, G, seen,blocked=set()):
  seen.add((r, c))
  for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < R and 0 <= nc < C \
       and (nr, nc) not in seen \
       and (nr, nc) not in blocked \
       and G[nr][nc] <= G[r][c]:
      dfs(nr, nc, R, C, G, seen, blocked)


def solve1(fname):
  lines = read_lines(fname)
  G = [list(line) for line in lines]
  R, C = len(G),len(G[0])
  seen = set()
  dfs(0,0,R,C,G,seen,set())
  return len(seen)


def solve2(fname):
  lines = read_lines(fname)
  G = [list(line) for line in lines]
  R, C = len(G),len(G[0])
  seen = set()
  dfs(0,0,R,C,G,seen)
  dfs(R-1,C-1,R,C,G,seen)
  return len(seen)


def solve3(fname):
  lines = read_lines(fname)
  G = [list(line) for line in lines]
  R, C = len(G),len(G[0])
  burnt = set()
  for _ in range(3):
    best_size, best_seen = 0, set()
    for r in range(R):
      for c in range(C):
        if (r,c) not in burnt:
          seen = set()
          dfs(r,c,R,C,G,seen,burnt)
          if len(seen) > best_size:
            best_size = len(seen)
            best_seen = seen
    for r,c in best_seen:
      burnt.add((r,c))
  return len(burnt)


def main():
  solvers = [solve1, solve2, solve3]
  for i, solve in enumerate(solvers, 1):
    start = time.time()
    ans = solve(f"in{i}.txt")
    elapsed = time.time() - start
    print(f"p{i}: {ans} ({elapsed:.3f}s)")


if __name__ == '__main__':
  main()
