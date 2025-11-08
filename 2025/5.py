import sys
import math
from pathlib import Path
from collections import deque, defaultdict, Counter


def read_input_lines(fname: str):
  file = Path(fname)
  if not file.exists():
    raise FileNotFoundError(f"Expected file '{fname}' not found!")
  return [ln.strip() for ln in file.read_text().splitlines() if ln.strip()]


class Node:
  def __init__(self, left=None, center=None, right=None):
    self.left = left
    self.center = center
    self.right = right
    self.next = None


  def __str__(self):
    parts = [str(x) for x in (self.left, f"[{self.center}]", self.right) if x is not None]
    return "-".join(parts) if parts else "Empty"


class TripleLinkedList:

  def __init__(self):
    self.head = None


  def add(self, num):
    if not self.head:
      self.head = Node(center=num)
      return
    curr = self.head
    while curr:
      if num < curr.center and curr.left is None:
        curr.left = num
        return
      if num > curr.center and curr.right is None:
        curr.right = num
        return
      if curr.next is None:
        curr.next = Node(center=num)
        return
      curr = curr.next


  def get_quality(self):
    cur, res = self.head, []
    while cur:
      res.append(str(cur.center))
      cur = cur.next
    return "".join(res)


  def get_rank(self):
    cur, res = self.head, []
    while cur:
      s = "".join(str(x) for x in (cur.left, cur.center, cur.right) if x is not None)
      res.append(int(s))
      cur = cur.next
    return res


  def print_list(self):
    if not self.head:
      print("Empty list")
      return
    curr = self.head
    node_index = 0
    while curr:
      parts = []
      if curr.left is not None:
        parts.append(str(curr.left))
      if curr.center is not None:
       parts.append(f"[{curr.center}]")
      if curr.right is not None:
       parts.append(str(curr.right))
      node_str = '-'.join(parts) if parts else "Empty"
      print(f"Node {node_index}: {node_str}")
      curr = curr.next
      node_index += 1


def solve1(fname):
  _, ri = read_input_lines(fname)[0].split(':')
  L = list(map(int, ri.split(',')))
  lst = TripleLinkedList()
  for num in L:
    lst.add(num)
  return lst.get_quality()


def solve2(fname):
  lines = read_input_lines(fname)
  mx, mn = -1, math.inf
  for line in lines:
    _, ri = line.split(':')
    L = list(map(int, ri.split(',')))
    lst = TripleLinkedList()
    for num in L:
      lst.add(num)
    quality = int(lst.get_quality())
    mx = max(quality, mx)
    mn = min(quality, mn)
  return mx-mn


def solve3(fname):
  lines = read_input_lines(fname)
  fish_bones = []
  for line in lines:
    id, ri = line.split(':')
    L = list(map(int, ri.split(',')))
    lst = TripleLinkedList()
    for num in L:
      lst.add(num)
    quality = lst.get_quality()
    fish_bones.append((int(quality), lst.get_rank(), int(id)))
  fish_bones.sort(reverse=True)
  return sum((i + 1) * f[2] for i, f in enumerate(fish_bones))


def main():
  for i, solve in enumerate([solve1, solve2, solve3], 1):
    print(f"p{i}:", solve(f"in{i}.txt"))


if __name__ == "__main__":
  main()
