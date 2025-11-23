import sys
from pathlib import Path

ST1 = 2025
ST2 = 2025_2025
ST3 = 2025_2025_2025


def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]


def solve1(fn):
  front, back = [], []
  for i, v in enumerate(map(int, read_lines(fn))):
    (front if i % 2 == 0 else back).append(v)
  L = [1] + front + back[::-1]
  return L[ST1 % len(L)]


def build(ls):
  n = len(ls)
  segs = [None]*(n+1)
  segs[0] = (1,1,1,False)
  frnt, back = 1, n
  tot = 1
  for i, s in enumerate(ls):
    a, b = map(int, s.split('-'))
    ln = b - a + 1
    tot += ln
    if i % 2 == 0:
      segs[frnt] = (a,b,ln,False)
      frnt += 1
    else:
      segs[back] = (a,b,ln,True)
      back -= 1
  return segs, tot


def value(segs, tot, steps):
  idx = steps % tot
  # print(f'{idx=}')
  for l,r,ln,rev in segs:
    if idx < ln:
      return (r - idx) if rev else (l + idx)
    idx -= ln


def solve2(fname, STEPS=ST2):
  L = read_lines(fname)
  segs, tot = build(L)
  return value(segs, tot, STEPS)


def solve3(fname):
  return solve2(fname, STEPS=ST3)


def main():
  for i, fn in enumerate([solve1, solve2, solve3], 1):
    print(f'p{i}:', fn(f'in{i}.txt'))


if __name__ == "__main__":
  main()
