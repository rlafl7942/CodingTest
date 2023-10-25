import sys

a = int(input())


for i in range(a):
  rank=0
  n, m = map(int, input().split())
  num=list(map(int, input().split()))

  index = [i for i in range(n)]
  
  while True:
    if max(num)>num[0]:
      num.append(num[0])
      del num[0]
      index.append(index[0])
      del index[0]
    else:
      rank+=1
      if index[0]==m:
        print(rank)
        break
      else:
        del index[0]
        del num[0]
