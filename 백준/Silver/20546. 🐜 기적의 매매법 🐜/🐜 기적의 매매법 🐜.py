import sys
from collections import deque

compare = deque()

input = sys.stdin.readline

def jun():
  left = money
  amount=0
  for i in range(len(chart)):
    if chart[i]<=left:
      tmp=0
      while True:
        if (tmp+1)*chart[i]<=left:
          tmp+=1
        else:
          break
      left=left-tmp*chart[i]
      amount+=tmp
  
  return left+amount*chart[13]

def min():
  left = money
  amount = 0
  for i in range(len(chart)-1):
    compare.append(chart[i])
    if len(compare)>=3:
      if compare[0]<compare[1] and compare[1]<compare[2]:
        left = left+amount*chart[i+1]
        amount=0
      elif compare[0]>compare[1] and compare[1]>compare[2]:
        tmp = 0
        while True:
          if (tmp+1)*chart[i+1]<=left:
            tmp+=1
          else:
            break
        amount+=tmp
        left = left-tmp*chart[i+1]
      compare.popleft()
      
  return left+amount*chart[13]


money = int(input())

chart = list(map(int, input().split()))

junProfit = jun()
minProfit = min()

if junProfit>minProfit:
  print("BNP")
elif junProfit<minProfit:
  print("TIMING")
else:
  print("SAMESAME")