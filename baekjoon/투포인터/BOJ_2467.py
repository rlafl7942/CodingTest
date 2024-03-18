import sys

input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

left = 0
right = n-1
sum = liquid[left]+liquid[right]
ans_left=left
ans_right=right

while left!=right:
  tmp = liquid[left]+liquid[right]
  if abs(sum)>abs(tmp):
    sum=tmp
    ans_left=left
    ans_right=right
  if tmp<0:
    left+=1
  else:
    right-=1

print(liquid[ans_left], liquid[ans_right])