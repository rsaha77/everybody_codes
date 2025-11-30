import sys
import time
from pathlib import Path

def read_lines(fname):
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fname)
  return [line.strip() for line in file.read_text().splitlines() if line.strip()]


def solve1(fname):
  L = read_lines(fname)
  L = list(map(int,L))

  tot = 10
  while tot >= 0:
    tot -= 1
    pL = L[:]
    for j in range(1, len(L)):
      i = j-1
      a, b = L[i], L[j]
      if a > b:
        L[i] -= 1
        L[j] += 1
    if pL == L:
      break

  while tot >= 0:
    tot -= 1
    pL = L[:]
    for j in range(1, len(L)):
      i = j-1
      a, b = L[i], L[j]
      if a < b:
        L[i] += 1
        L[j] -= 1
    if pL == L:
      break

  ans = 0
  for i,n in enumerate(L):
    ans += (i+1) * n
  return ans


def solve2(fname):
  L = read_lines(fname)
  L = list(map(int,L))
  rounds=0

  while True:
    pL = L[:]
    for j in range(1, len(L)):
      i = j-1
      a, b = L[i], L[j]
      if a > b:
        L[i] -= 1
        L[j] += 1
    if pL == L:
      break
    rounds += 1

  while True:
    pL = L[:]
    for j in range(1, len(L)):
      i = j-1
      a, b = L[i], L[j]
      if a < b:
        L[i] += 1
        L[j] -= 1
    if pL == L:
      break
    rounds += 1

  return rounds


def main():
  for i, solver in enumerate([solve1, solve2], 1):
    print(f'p{i}:', solver(f'in{i}.txt'))



if __name__ == "__main__":
  main()
