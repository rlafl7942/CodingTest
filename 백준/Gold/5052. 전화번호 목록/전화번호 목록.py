import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  tmp = []
  n = int(input())
  for _ in range(n):
    tmp.append((input().rstrip()))
  tmp = sorted(tmp)
  flag = 0
  for i in range(len(tmp)-1):
    if tmp[i+1].startswith(tmp[i]):
      flag = 1
    
  if flag == 1:
    print("NO")
  else:
    print("YES")