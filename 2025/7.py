import sys
from pathlib import Path
from collections import defaultdict


def read_input_lines(file_name):
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(file_name)
  if not file.exists():
    raise FileNotFoundError(f"Expected file '{file}' not found!")
  return [line.strip() for line in file.read_text().splitlines() if line.strip()]


def is_valid(name, D):
  for i in range(1, len(name)):
    if name[i] not in D[name[i - 1]]:
      return False
  return True


def dfs(D, path, length, result):
  if 7 <= length <= 11:
    result.add(''.join(path))
  if length >= 11:
    return

  last_ch = path[-1]
  if last_ch in D:
    for next_ch in D[last_ch]:
      path.append(next_ch)
      dfs(D, path, length + 1, result)
      path.pop()


def parse_rules(lines):
  D = defaultdict(list)
  for line in lines[1:]:
    left, right = [x.strip() for x in line.split('>')]
    for ch in right.split(','):
      D[left].append(ch.strip())
  return D


def solve1(fname):
  lines = read_input_lines(fname)
  names = lines[0].split(',')
  D = parse_rules(lines)

  for name in names:
    if is_valid(name, D):
      return name


def solve2(fname):
  lines = read_input_lines(fname)
  names = lines[0].split(',')
  D = parse_rules(lines)

  return sum(i + 1 for i, name in enumerate(names) if is_valid(name, D))


def solve3(fname):
  lines = read_input_lines(fname)
  prefixes = lines[0].split(',')
  D = parse_rules(lines)

  all_names = set()
  for prefix in prefixes:
    if is_valid(prefix, D):
      names = set()
      dfs(D, list(prefix), len(prefix), names)
      all_names.update(names)

  return len(all_names)


def main():
  solvers = [solve1, solve2, solve3]
  for i, solve in enumerate(solvers, 1):
    print(f"p{i}:", solve(f"in{i}.txt"))


if __name__ == "__main__":
  main()
