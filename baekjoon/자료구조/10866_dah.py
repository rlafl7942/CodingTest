import sys
input = sys.stdin.readline
from collections import deque

deque = deque([])

n = int(input())

for i in range(n):
    s = input().split()
    if s[0] == "push_front":
        deque.appendleft(int(s[-1]))
    elif s[0] == "push_back":
        deque.append(int(s[-1]))
    elif s[0] == "pop_front":
        print(-1) if len(deque) == 0 else print(deque.popleft())
    elif s[0] == "pop_back":
        print(-1) if len(deque) == 0 else print(deque.pop())
    elif s[0] == "size":
        print(len(deque))
    elif s[0] == "empty":
        print(1) if len(deque) == 0 else print(0)
    elif s[0] == "front":
        print(-1) if len(deque) == 0 else print(deque[0])
    elif s[0] == "back":
        print(-1) if len(deque) == 0 else print(deque[-1])

