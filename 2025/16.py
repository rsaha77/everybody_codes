import sys
from pathlib import Path
from functools import lru_cache
from typing import List, Tuple

BLOCKS = 2025_2025_2025_000

def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]

def facts(n):
  r = []
  i = 1
  while i * i <= n:
    if n % i == 0:
      r.append(i)
      if n // i != i:
        r.append(n // i)
    i += 1
  return r


def can(spell, blocks, wl):
  return sum(wl // x for x in spell) <= blocks


def b_search(spell, BLOCKS):
  lo, hi = 1, BLOCKS
  while lo <= hi:
    wall_length = (lo + hi) // 2
    if can(spell, BLOCKS, wall_length):
      lo = wall_length + 1
    else:
      hi = wall_length - 1
  return hi


def solve1(fname):
  lines = read_lines(fname)
  spell = list(map(int,lines[0].split(',')))
  return sum(90 // x for x in spell)


def p2_and_spell(lines):
  L = list(map(int, lines[0].split(',')))
  rem = []
  for i, blocks in enumerate(L):
    col = i + 1
    for fact in facts(col):
      if fact < col:
        blocks -= rem[fact - 1]
    rem.append(blocks)
  ans = 1
  spell = []
  for i, r in enumerate(rem):
    if r > 0:
      ans *= i + 1
      spell.append(i + 1)
  return ans, spell


def solve2(fname):
  lines = read_lines(fname)
  ans, _ = p2_and_spell(lines)
  return ans


def solve3(fname):
  lines = read_lines(fname)
  _, spell = p2_and_spell(lines)
  return b_search(spell, BLOCKS)


def main():
  for i, fn_solver in enumerate([solve1, solve2, solve3], 1):
    print(f'p{i}:', fn_solver(f'in{i}.txt'))


if __name__ == "__main__":
  main()
