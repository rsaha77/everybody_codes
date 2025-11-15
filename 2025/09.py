import sys
import time
from pathlib import Path
from collections import defaultdict

def read_input_lines(fname):
  file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fname)
  return [line.strip() for line in file.read_text().splitlines() if line.strip()]


class DSU:
  def __init__(self, n):
    self.par = list(range(n))
    self.siz = [1] * n

  def get_par(self, x):
    if self.par[x] != x:
      self.par[x] = self.get_par(self.par[x])
    return self.par[x]

  def join(self, a, b):
      a, b = self.get_par(a), self.get_par(b)
      if a == b:
          return False
      if self.siz[a] < self.siz[b]:
          a, b = b, a
      self.siz[a] += self.siz[b]
      self.par[b] = a
      return True

  def is_connected(self, a, b):
    return self.get_par(a) == self.get_par(b)

  def get_component_size(self, x):
    return self.siz[self.get_par(x)]

  def get_component_nodes(self, x):
      root = self.get_par(x)
      return [i for i in range(len(self.par)) if self.get_par(i) == root]


def is_valid_child(child, p1, p2):
  return all(c == p or c == q for c, p, q in zip(child, p1, p2))


def get_degree (child, p1, p2):
  m1 = sum(c == p for c, p in zip(child, p1))
  m2 = sum(c == q for c, q in zip(child, p2))
  return m1 * m2


def solve1(fname):
    lines = read_input_lines(fname)
    seqs = [line.split(':')[1] for line in lines]

    for combo in [(0,1,2), (1, 0, 2), (2, 0, 1)]:
        child_idx, p1_idx, p2_idx = combo
        if is_valid_child(seqs[child_idx], seqs[p1_idx], seqs[p2_idx]):
            return get_degree (seqs[child_idx], seqs[p1_idx], seqs[p2_idx])


def solve2(fname):
  lines = read_input_lines(fname)
  L = [line.split(':')[1] for line in lines]
  N = len(L)
  ans = 0
  for i in range(N):
    for j in range(N):
      for k in range(N):
        if i != j and i != k:
          if is_valid_child(L[i], L[j], L[k]):
            ans += get_degree(L[i], L[j], L[k])
  return ans // 2


def solve3(fname):
  lines = read_input_lines(fname)
  L = [line.split(':')[1] for line in lines]
  N = len(L)
  dsu = DSU(N)
  for i in range(N):
    for j in range(i+1, N):
      for k in range(j+1, N):
        for child, p1, p2 in [(i, j, k), (j, i, k), (k, i, j)]:
          if is_valid_child(L[child], L[p1], L[p2]):
            dsu.join(i, j)
            dsu.join(i, k)
  mx = alpha = 0
  for i in range(N):
    sz = dsu.get_component_size(i)
    if mx < sz:
      mx = sz
      alpha = i
  return sum(x + 1 for x in dsu.get_component_nodes(alpha))


def main():
  solvers = [solve1, solve2, solve3]
  for i, solve in enumerate(solvers, 1):
    start = time.time()
    ans = solve(f"in{i}.txt")
    elapsed = time.time() - start
    print(f"p{i}: {ans} ({elapsed:.3f}s)")


if __name__ == "__main__":
  main()
