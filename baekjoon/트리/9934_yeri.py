import sys

input = sys.stdin.readline

def makeTree(arr, level):
  mid = len(arr)//2
  tree[level].append(arr[mid])

  if len(arr) == 1:
    return
  
  makeTree(arr[:mid], level+1)
  makeTree(arr[mid+1:], level+1)

k = int(input())
building = list(map(int, input().split()))
tree=[[] for _ in range(k)]

makeTree(building, 0)

for i in tree:
  print(*i)