import sys

input = sys.stdin.readline

n = int(input())

tips=[]

for _ in range(n):
  tips.append(int(input()))

tips.sort(reverse=True)
for i in range(len(tips)):
  tips[i]-=i
  if tips[i]<0:
    tips[i]=0
print(sum(tips))

