import sys
import time
from pathlib import Path


def read_input_lines(fname):
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fname)
  return [line.strip() for line in file.read_text().splitlines() if line.strip()]


def can_cut(P, Q, a, b):
  if a > b:
    a, b = b, a
  if a in [P,Q] or b in [P,Q] or (P < a < Q and P < b < Q) or (not P < a < Q and not P < b < Q):
    return False
  return True


def solve1(fname):
  lines = read_input_lines(fname)
  L = [int(x) for x in lines[0].split(',')]
  ans = 0
  N = 32
  half = N // 2
  for i in range(1, len(L)):
    if abs(L[i] - L[i-1]) == half:
      ans += 1
  return ans


def solve2(fname):
  lines = read_input_lines(fname)
  L = [int(x) for x in lines[0].split(',')]
  knots = 0
  for i in range(2, len(L)):
    P, Q = min(L[i], L[i-1]), max(L[i], L[i-1])
    for a,b in zip(L[:i], L[1:i]):
      if can_cut(P, Q, a, b):
        knots += 1
  return knots


def solve3(fname):
  lines = read_input_lines(fname)
  L = [int(x) for x in lines[0].split(',')]
  # N = 8
  N = 256
  max_cuts = 0
  for P in range (1, N+1):
    for Q in range (P+1, N+1):
      curr_cuts = 0
      for a,b in zip(L, L[1:]):
        if can_cut (P, Q, a, b):
          curr_cuts += 1
        if [a,b] == [P,Q] or [a,b] == [Q,P]:
          curr_cuts += 1
      max_cuts = max(max_cuts, curr_cuts)
  return max_cuts


def main():
  solvers = [solve1, solve2, solve3]
  for i, solve in enumerate(solvers, 1):
    start = time.time()
    ans = solve(f"in{i}.txt")
    elapsed = time.time() - start
    print(f"p{i}: {ans} ({elapsed:.3f}s)")


if __name__ == "__main__":
  main()
