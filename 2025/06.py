from pathlib import Path

def read_input(fname):
  return Path(fname).read_text().strip()

def solve1(fname):
  s = read_input(fname)
  ans, A = 0, 0
  for x in s:
    if x == 'A': A += 1
    if x == 'a': ans += A
  return ans

def solve2(fname):
  s = read_input(fname)
  ans = 0
  cnt = {'A': 0, 'B': 0, 'C': 0}
  for x in s:
    if x in 'ABC': cnt[x] += 1
    if x in 'abc': ans += cnt[x.upper()]
  return ans

def solve3(fname):
  s = read_input(fname) * 1000
  ln, lim, ans = len(s), 1000, 0

  # Forward
  cnt = {'A': [0] * ln, 'B': [0] * ln, 'C': [0] * ln}
  for i in range(ln):
    for ch in 'ABC':
      cnt[ch][i] = (s[i] == ch) + (cnt[ch][i-1] if i > 0 else 0)
    if s[i] in 'abc':
      mentor = s[i].upper()
      left = max(0, i - lim)
      ans += cnt[mentor][i] - (cnt[mentor][left-1] if left > 0 else 0)

  # Backward
  cnt = {'A': [0] * ln, 'B': [0] * ln, 'C': [0] * ln}
  for i in range(ln-1, -1, -1):
    for ch in 'ABC':
      cnt[ch][i] = (s[i] == ch) + (cnt[ch][i+1] if i < ln-1 else 0)
    if s[i] in 'abc':

      mentor = s[i].upper()
      right = min(ln-1, i + lim)
      ans += cnt[mentor][i] - (cnt[mentor][right+1] if right < ln-1 else 0)

  return ans

def main():
  for i, solve in enumerate([solve1, solve2, solve3], 1):
    print(f"p{i}:", solve(f"in{i}.txt"))

if __name__ == "__main__":
  main()
