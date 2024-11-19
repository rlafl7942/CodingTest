import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

score.sort()

result = 0

for i in range(n-2):
  left, right = i+1, n-1
  while left<right:
    tmp = score[i] + score[left] + score[right]
    if tmp > 0:
      right -= 1
    else:
      if tmp == 0:
        if score[left] == score[right]:
          result += right- left
        else:
          index = bisect_left(score, score[right])
          result += right - index + 1
      left += 1
print(result)