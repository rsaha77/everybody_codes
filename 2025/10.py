import sys
import time
from pathlib import Path

def read_input_lines(fname):
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fname)
  return [line.strip() for line in file.read_text().splitlines() if line.strip()]


KNIGHT_MOVES = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
def get_knight_moves(r, c, R, C):
  return [(r+dr, c+dc) for dr, dc in KNIGHT_MOVES if 0 <= r+dr < R and 0 <= c+dc < C]


def move_sheep(s, R, C):
  ns = [[False for _ in range(C)] for _ in range(R)]
  for r in range(R-1):
    for c in range(C):
      if s[r][c]:
        ns[r+1][c] = True
  return ns


def count_eaten_sheep(pts, sheep, hide):
  eaten = 0
  for r, c in pts:
    if sheep[r][c] and not hide[r][c]:
      eaten += 1
      sheep[r][c] = False
  return eaten


def solve1(fname):
  lines = read_input_lines(fname)
  grid = [list(line) for line in lines]
  R, C = len(grid), len(grid[0])

  dragon = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 'D']
  pts = dragon
  reach = [['.' for _ in range(C)] for _ in range(R)]

  for _ in range(4):
    new_pts = set()
    for r, c in pts:
      new_pts.update(get_knight_moves(r, c, R, C))
    for r, c in new_pts:
      reach[r][c] = 'X'
    pts = new_pts

  ans = 0
  for r in range(R):
    for c in range(C):
      if reach[r][c] == 'X' and grid[r][c] == 'S':
        ans += 1
  return ans


def solve2(fname):
  lines = read_input_lines(fname)
  sheep, hide = [], []
  dragon = []

  for r, line in enumerate(lines):
    sheep.append([x == 'S' for x in line])
    hide.append([x == '#' for x in line])
    for c, x in enumerate(line):
      if x == 'D':
        dragon = [(r, c)]

  R, C = len(sheep), len(sheep[0])
  eaten = 0

  for _ in range(20):
    new_dragon = set()
    for r, c in dragon:
      new_dragon.update(get_knight_moves(r, c, R, C))

    eaten += count_eaten_sheep(new_dragon, sheep, hide)
    sheep = move_sheep(sheep, R, C)
    eaten += count_eaten_sheep(new_dragon, sheep, hide)
    dragon = new_dragon

  return eaten


def main():
  solvers = [solve1, solve2]
  for i, solve in enumerate(solvers, 1):
    start = time.time()
    ans = solve(f"in{i}.txt")
    elapsed = time.time() - start
    print(f"p{i}: {ans} ({elapsed:.3f}s)")


if __name__ == "__main__":
  main()
