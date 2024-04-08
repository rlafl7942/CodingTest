import sys

input = sys.stdin.readline

n = int(input())

check=[0] * 366

for _ in range(n):
  s, e = map(int, input().split())

  for i in range(s, e+1):
    check[i]+=1

max_check = 0
days = 0
answer = 0
for i in check:
  if i!=0:
    days += 1
    max_check = max(i, max_check)
  else:
    answer += max_check * days
    days = 0
    max_check = 0

print(answer)