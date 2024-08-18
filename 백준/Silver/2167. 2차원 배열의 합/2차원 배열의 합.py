import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = []
inputNumbers = []

for i in range(n):
  inputNumbers = list(map(int, input().split()))
  numbers.append(inputNumbers)

k = int(input())
for _ in range(k):
  i, j, x, y = map(int, input().split())
  sum = 0
  for a in range(i-1, x):
    for b in range(j-1, y):
      sum += numbers[a][b]
  print(sum)