import sys
from pathlib import Path
from collections import deque, defaultdict, Counter

def read_input_lines():
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("in.txt")
  if not file.exists():
      raise FileNotFoundError(f"Expected file '{file}' not found!")
  lines = [line.strip() for line in file.read_text().splitlines() if line.strip()]
  return lines


def solve3(names, instructions):
  for inst in instructions:
    drc, cnt = inst[0], int(inst[1:])
    new_pos = (cnt if drc == 'R' else -cnt) % len(names)
    names[0], names[new_pos] = names[new_pos], names[0]
  return names[0]


def main():
  lines = read_input_lines()
  names = lines[0].split(',')
  instructions = lines[1].split(',')

  ptr1, ptr2 = 0, 0
  for inst in instructions:
    drc, cnt = inst[0], int(inst[1:])
    if drc == 'R':
      ptr1 = min (len(names)-1, ptr1 + cnt)
      ptr2 = (ptr2 + cnt) % len(names)
    else:
      ptr1 = max (0, ptr1 - cnt)
      ptr2 = (ptr2 - cnt) % len(names)
  print("p1: ", names[ptr1])
  print("p2: ", names[ptr2])
  print("p3: ", solve3(names, instructions))


if __name__ == "__main__":
  main()

