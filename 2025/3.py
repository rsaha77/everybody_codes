import sys
from pathlib import Path
from collections import deque, defaultdict, Counter

def read_input_lines():
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("in.txt")
  if not file.exists():
      raise FileNotFoundError(f"Expected file '{file}' not found!")
  lines = [line.strip() for line in file.read_text().splitlines() if line.strip()]
  return lines


def main():
  lines = read_input_lines()
  L = sorted(set(list(map(int, lines[0].split(',')))))

  print("p1: ", sum(L))

  sm = 0
  for i in range(20):
    sm += L[i]
  print("p2: ", sm)

  L = sorted(list(map(int, lines[0].split(','))))
  prev, cnt, mx = -1, 0, 0
  for l in L:
    if l == prev:
      cnt += 1
      if cnt > mx:
        mx = cnt
    else:
      cnt = 0
    prev = l
  print("p2: ", mx + 1)


if __name__ == "__main__":
  main()

