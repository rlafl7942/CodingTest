import sys
from collections import deque

input = sys.stdin.readline

n, k= map(int, input().split())

arr = deque()
ans = []

for i in range(n):
  arr.append(i+1)

# deq rotate 사용
while arr:
  arr.rotate(-(k-1))
  tmp = arr.popleft()
  ans.append(tmp)

# <> 추가하기
result = "<"
cnt = 0
for i in ans:
  result += str(i)
  cnt+=1
  if cnt!=n:
    result += ", "
result += ">"

print(result)