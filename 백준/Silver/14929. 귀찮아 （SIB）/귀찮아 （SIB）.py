import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
tmp = sum(numbers)
presum = 0
for i in range(len(numbers)):
  tmp -= numbers[i]
  presum += tmp * numbers[i]
print(presum)