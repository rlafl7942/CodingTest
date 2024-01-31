import sys
from collections import defaultdict


n = int(input())
tree=defaultdict(list)

for _ in range(n-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

q = int(input())

for _ in range(q):
  t, k = map(int, input().split())
  if t == 1:
    if len(tree[k]) < 2:
      print("no")
    else:
      print("yes")
  else:
    print("yes")
