import sys
import math
from pathlib import Path
from collections import deque, defaultdict, Counter

def read_input_lines(file_name):
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(file_name)
  if not file.exists():
      raise FileNotFoundError(f"Expected file '{file}' not found!")
  lines = [line.strip() for line in file.read_text().splitlines() if line.strip()]
  return lines

def solve1(fname):
  L = list(map(int, read_input_lines(fname)))
  print("p1: ", math.floor(2025*(L[0]/L[-1])))


def solve2(fname):
  L = list(map(int, read_input_lines(fname)))
  print("p2: ", math.ceil(10000000000000/(L[0]/L[-1])))


def solve3(fname):
  lines = read_input_lines(fname)
  prev = int(lines[0])
  rot = 1
  for s in lines[1:-1]:
    a, b = [int(x) for x in s.split('|')]
    rot = rot * (prev/a)
    prev = b
  print("p3: ", math.floor(100 * rot * (int(lines[-2].split('|')[1]) / int(lines[-1]))))
    


def main():
  solve1("in1.txt")
  solve2("in2.txt")
  solve3("in3.txt")


if __name__ == "__main__":
  main()

