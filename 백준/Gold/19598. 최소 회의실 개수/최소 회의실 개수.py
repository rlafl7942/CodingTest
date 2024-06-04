import sys, heapq

input = sys.stdin.readline

meetings = []
h = []

n = int(input())
for i in range(n):
  start, end = map(int, input().split())
  meetings.append([start, end])

meetings = sorted(meetings)

for start,end in meetings:
  if h and h[0] <= start:
    heapq.heappop(h)
  heapq.heappush(h, end)

print(len(h))