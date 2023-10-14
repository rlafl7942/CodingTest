from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
q = deque()  # *

for _ in range(n):
    s = list(input().split())
    if s[0] == "push":
        q.append(int(s[-1]))
    elif s[0] == "pop":
        print(-1) if len(q) == 0 else print(q.popleft())  # *
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        print(1) if len(q) == 0 else print(0)
    elif s[0] == "front":
        print(-1) if len(q) == 0 else print(q[0])
    elif s[0] == "back":
        print(-1) if len(q) == 0 else print(q[-1])