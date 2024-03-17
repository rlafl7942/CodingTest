import sys

input = sys.stdin.readline

n, x = map(int, input().split())

visitors = list(map(int, input().split()))

tmp = sum(visitors[:x])
max_sum = tmp
cnt = 1

for i in range(x,n):
  tmp -= visitors[i-x] # 앞에꺼 빼주고
  tmp += visitors[i] # 뒤에꺼 더해주기
  if tmp>max_sum:
    max_sum=tmp
    cnt=1 # cnt 초기화
  elif tmp==max_sum:
    cnt+=1

if max_sum==0:
  print("SAD")
else:
  print(max_sum)
  print(cnt)