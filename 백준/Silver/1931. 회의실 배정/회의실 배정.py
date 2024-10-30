import sys

input = sys.stdin.readline

n = int(input())

times = []
answer = 0
current_end = 0

for _ in range(n):
  times.append(list(map(int, input().split())))

times = sorted(times, key = lambda x : (x[1], x[0]))

for time in times:
  if time[0] >= current_end:
    current_end = time[1]
    answer += 1
print(answer)