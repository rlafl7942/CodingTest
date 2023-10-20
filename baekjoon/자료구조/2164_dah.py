import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

list_ = deque([i for i in range(1, n+1)])

while len(list_) > 1:
    list_.popleft()
    list_.append(list_.popleft())

print(*list_)
