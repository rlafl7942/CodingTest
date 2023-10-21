import sys
from collections import deque

deque = deque()

n = int(input())
for i in range(n):
  order = sys.stdin.readline().split()
  if order[0]=="push_front":
    deque.appendleft(order[-1])
  elif order[0]=="push_back":
    deque.append(order[-1])
  elif order[0]=="pop_front":
    if len(deque)!=0:
      print(deque.popleft())
    else:
      print(-1)
  elif order[0]=="pop_back":
    if len(deque)!=0:
      print(deque.pop())
    else:
      print(-1)
  elif order[0]=="size":
    print(len(deque))
  elif order[0]=="empty":
    if len(deque)==0:
      print(1)
    else:
      print(0)
  elif order[0]=="front":
    if len(deque)!=0:
      print(deque[0])
    else:
      print(-1)
  elif order[0]=="back":
    if len(deque)!=0:
      print(deque[-1])
    else:
      print(-1)
