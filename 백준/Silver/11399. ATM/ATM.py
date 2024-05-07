import sys

input = sys.stdin.readline

n = int(input())

withdraw = list(map(int, input().split()))

withdraw.sort()

for i in range(1, len(withdraw)):
  withdraw[i] += withdraw[i-1]

print(sum(withdraw))