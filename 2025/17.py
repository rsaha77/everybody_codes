import sys
from pathlib import Path


def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]


def parse(lines):
  G, Rv, Cv = [], -1, -1
  for r, line in enumerate(lines):
    G.append(line)
    for c, ch in enumerate(line):
      if ch == '@':
        Rv, Cv = r, c
  assert ([Rv, Cv] != [-1, -1])
  return G, Rv, Cv


def solve1(fname):
  lines = read_lines(fname)
  G, Rv, Cv = parse(lines)
  R, C = len(G), len(G[0])
  ans, Radius = 0, 10
  r2 = Radius * Radius
  for r in range(R):
    for c in range(C):
      if r == Rv and c == Cv:
        continue
      dr, dc = Rv - r, Cv - c
      if dr * dr + dc * dc <= r2:
        ans += int(G[r][c])
  return ans


def solve2(fname):
  lines = read_lines(fname)
  G, Rv, Cv = parse(lines)
  R, C = len(G), len(G[0])
  max_damage, prev_damage, ans = 0, 0, 0
  for Radius in range(R // 2):
    damage = -prev_damage
    r2 = Radius * Radius
    for r in range(R):
      for c in range(C):
        if r == Rv and c == Cv:
          continue
        dr, dc = Rv - r, Cv - c
        if dr * dr + dc * dc <= r2:
          damage += int(G[r][c])
    if damage > max_damage:
      ans = damage * Radius
      max_damage = damage
    prev_damage += damage
  return ans


def main():
  for i, fn in enumerate([solve1, solve2], 1):
    print(f'p{i}:', fn(f'in{i}.txt'))


if __name__ == "__main__":
  main()
