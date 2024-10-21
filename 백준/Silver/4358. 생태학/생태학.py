from collections import deque, defaultdict
import sys

input = sys.stdin.readline

trees = defaultdict(int)
total = 0

while True:
  in_tree = input().strip()
  if not in_tree:
    break
  trees[in_tree] += 1
  total += 1

trees_sort = sorted(trees)

for tree in trees_sort:
  print("%s %.4f" %(tree, trees[tree]/total * 100))