import sys
from collections import deque

n = int(input())

# 시간 초과.. 
# 리스트 옮기는데에 시간이 걸림
# card = list(range(1,n+1))

# while len(card)!=1:
#   del card[0]
#   card.append(card[0])
#   del card[0]


# print(card[0])

deque = deque(range(1,n+1))

while len(deque)!=1:
  deque.popleft()
  deque.append(deque.popleft())

print(deque[0])