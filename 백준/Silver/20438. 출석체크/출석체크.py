import sys
from collections import Counter
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
students = [0] * (n+3)

sleeping = set(map(int, input().split()))
receiver = set(map(int, input().split()))

for value in (receiver-sleeping):
  for i in range(value, n+3, value):
    if i not in sleeping:
      students[i] = 1

attend = [0] * (n+3)
for i in range(3, n+3):
  attend[i] = attend[i-1]+students[i]

for i in range(m):
  s, e = map(int, input().split())
  print(e-s+1-(attend[e]-attend[s-1]))