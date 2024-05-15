import sys

input = sys.stdin.readline

n, k = map(int, input().split())
height = list(map(int, input().split()))

array = []
for i in range(1,n):
  array.append(height[i] - height[i-1])

array.sort(reverse=True)
print(sum(array[k-1:]))