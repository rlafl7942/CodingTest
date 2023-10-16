import sys
from collections import deque

stack=[]
cnt = 0 #pop을 위한 변수

n = int(input())
for i in range(n):
  order = list(sys.stdin.readline().split())
  if order[0]=="push":
    stack.append(order[-1])
  elif order[0]=="pop":
    if len(stack)-cnt==0:
      print(-1)
    else:
      #print(stack.pop(0))
      print(stack[cnt])
      cnt+=1
  elif order[0]=="size":
    print(len(stack)-cnt)
  elif order[0]=="empty":
    if len(stack)-cnt==0:
      print(1)
    else:
      print(0)
  elif order[0]=="front":
    if len(stack)-cnt==0:
      print(-1)
    else:
      print(stack[cnt])
  elif order[0]=="back":
    if len(stack)-cnt==0:
      print(-1)
    else:
      print(stack[-1])

# 리스트로 선언해서 Pop(0)을 하게 되면
# 첫 번째 요소를 pop 하고 나서 앞으로 당기는 데에 시간 초과
# -> cnt로 가리키기






# deque 라이브러리 이용
# deque = deque()

# n = int(input())
# for i in range(n):
#   order = list(sys.stdin.readline().split())
#   if order[0]=="push":
#     deque.append(order[-1])
#   elif order[0]=="pop":
#     if len(deque)==0:
#       print(-1)
#     else:
#       print(deque.popleft())
#   elif order[0]=="size":
#     print(len(deque))
#   elif order[0]=="empty":
#     if len(deque)==0:
#       print(1)
#     else:
#       print(0)
#   elif order[0]=="front":
#     if len(deque)==0:
#       print(-1)
#     else:
#       print(deque[0])
#   elif order[0]=="back":
#     if len(deque)==0:
#       print(-1)
#     else:
#       print(deque[-1])