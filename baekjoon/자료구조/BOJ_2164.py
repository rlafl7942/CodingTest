import sys
from collections import deque

input = sys.stdin.readline
q = deque()

n = int(input())

for i in range(n):
  q.append(i+1)

while len(q)!=1:
  q.popleft()
  tmp = q.popleft()
  q.append(tmp)

print(q[0])