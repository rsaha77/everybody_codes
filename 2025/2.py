import sys
from pathlib import Path
from collections import deque, defaultdict, Counter

def read_input_lines():
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("in.txt")
  if not file.exists():
      raise FileNotFoundError(f"Expected file '{file}' not found!")
  lines = [line.strip() for line in file.read_text().splitlines() if line.strip()]
  return lines


def get_res(R, A, div):
  X1, Y1, X2, Y2 = R[0], R[1], R[0], R[1]
  X1, Y1 = X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2
  X1 = int(X1 / div)
  Y1 = int(Y1 / div)
  X1, Y1 = X1 + A[0], Y1 + A[1]
  return [X1, Y1]

def solve1():
  R = [0, 0]
  # SAMPLE = [25,9]
  # A = SAMPLE
  A=[163,55]
  n = 3
  for _ in range(3):
    R = get_res(R, A, 10)

  return [R[0], R[1]]


def solve2(jmp):
  # SAMPLE =[35300,-64910]
  # A = SAMPLE
  A=[-79735,15616]
  x1, x2 = A[0], A[0] + 1000
  y1, y2 = A[1], A[1] + 1000
  MAX_N = 1_000_000

  ans = 0
  rr=[]
  for y in range(y1, y2 + 1, jmp):
    for x in range(x1, x2 + 1, jmp):
      R = [0, 0]
      can = True
      for _ in range(100):
        R = get_res(R, [x,y], 100000)
        if not (-MAX_N <= R[0] <= MAX_N and -MAX_N <= R[1] <= MAX_N):
          can = False
          break
      if can:
        rr.append((x, y))
        ans += 1

  return ans


def main():
  print("p1: ", solve1())
  print("p2: ", solve2(10))
  print("p3: ", solve2(1))

if __name__ == "__main__":
  main()
