import sys

input = sys.stdin.readline

n = int(input())

result = 0

# 2를 계속 빼주고 5로 나누어떨어지면 break
# n이 음수가 되면 거슬러 줄 수 없는 수

while n>0:
  if n%5==0: 
    result += n//5
    break
  else: 
    n-=2
    result+=1
  
if n<0:
  print(-1)
else:
  print(result)