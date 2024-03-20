import sys

input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

tmp_a = []
tmp_b = []

tmp = -1
for i in block:
  if i >= tmp:
    tmp = i
  tmp_a.append(tmp)

tmp = -1
for i in range(len(block)-1, -1, -1):
  if block[i] >= tmp:
    tmp = block[i]
  tmp_b.append(tmp)

sum = 0
for i in range(len(block)):
  tmp = min(tmp_a[i], tmp_b[len(block)-1-i])
  if block[i] < tmp:
    sum += tmp - block[i]

print(sum)