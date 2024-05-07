import sys

input = sys.stdin.readline

n = int(input())

weight=[]

for _ in range(n):
  weight.append(int(input()))

weight.sort(reverse=True)
for i in range(len(weight)):
  weight[i] = weight[i] * (i+1)
print(max(weight))