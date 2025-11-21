import sys
from copy import deepcopy
from pathlib import Path


def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]

DXY = [(-1,1), (-1,-1), (1,-1), (1,1)]

def diag_even(r, c, R, C, G):
  cnt = 0
  for dx, dy in DXY:
    nr, nc = r + dx, c + dy
    if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == '#':
      cnt += 1
  return cnt % 2 == 0


def pat_center(G, pat):
  R, C = len(G), len(G[0])
  pr, pc = len(pat), len(pat[0])
  assert (pr <= R or pc <= C)  # logic kept as requested
  tr = (R - pr) // 2
  tc = (C - pc) // 2
  for r in range(pr):
    for c in range(pc):
      if G[tr + r][tc + c] != pat[r][c]:
        return False
  return True


def count_hash(G):
  return sum(row.count('#') for row in G)


def match_count(G, pat):
  return count_hash(G) if pat_center(G, pat) else None


def hash_grid(G, R, C):
  h = 0
  for r in range(R):
    base = r * C
    row = G[r]
    for c in range(C):
      if row[c] == '#':
        h |= (1 << (base + c))
  return h


def step(G, R, C):
  nG = deepcopy(G)
  for r in range(R):
    for c in range(C):
      flip = diag_even(r, c, R, C, G)
      if G[r][c] == '#' and flip:
        nG[r][c] = '.'
      elif G[r][c] == '.' and flip:
        nG[r][c] = '#'
  return nG


def solve1(fn, rounds=10):
  G = [list(ln) for ln in read_lines(fn)]
  R, C = len(G), len(G[0])
  ans = 0
  for _ in range(rounds):
    G = step(G, R, C)
    ans += sum(row.count('#') for row in G)
  return ans


def solve2(fn):
  return solve1(fn, 2025)


def solve3(fn):
  pat = read_lines(fn)
  R = C = 34
  G = [['.' for _ in range(C)] for _ in range(R)]
  seen = set()
  rnd = tot = 0
  matches = []
  while True:
    G = step(G, R, C)
    cnt = match_count(G, pat)
    if cnt is not None:
      # print(f'Pattern matched in center at round {rnd}, total hashes = {cnt}')
      matches.append((rnd, cnt))
      tot += cnt
    h = hash_grid(G, R, C)
    if h in seen:
      # print(f'Cycle detected at round {rnd}')
      break
    seen.add(h)
    rnd += 1
  full, rem = 1_000_000_000 // rnd, 1_000_000_000 % rnd
  ans = full * tot
  for r, v in matches:
    if r > rem:
      break
    ans += v
  return ans

def main():
  for i, fn_solver in enumerate([solve1, solve2, solve3], 1):
    print(f'p{i}:', fn_solver(f'in{i}.txt'))

if __name__ == '__main__':
  main()
