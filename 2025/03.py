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
  L = list(map(int, lines[0].split(',')))

  unique_nums = sorted(set(L))
  
  print("p1: ", sum(unique_nums))
  print("p2: ", sum(unique_nums[:20]))

  freq = Counter(L)
  print("p3: ", max(freq.values()))


if __name__ == "__main__":
  main()

