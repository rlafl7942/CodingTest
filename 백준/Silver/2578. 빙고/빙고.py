import sys

input = sys.stdin.readline

def check():
  bingo = 0
  cnt = 0
  for i in range(5):
    if chul[i] == [0] * 5:
      bingo+=1
  
  for i in range(5):
    cnt=0
    for j in range(5):
      if chul[j][i] == 0:
        cnt+=1
    if cnt==5:
      bingo+=1
  
  if all(chul[i][i]==0 for i in range(5)):
    bingo+=1
  
  if all(chul[i][4-i]==0 for i in range(5)):
    bingo+=1
  
  return bingo



host = []
chul = []

for _ in range(5):
  numbers = list(map(int, input().split()))
  chul.append(numbers)

for _ in range(5):
  host += list(map(int, input().split()))

cnt = 0
for a in range(len(host)):
  for i in range(5):
    for j in range(5):
      if host[a] == chul[i][j]:
        chul[i][j] = 0
        cnt+=1

  if cnt>=12:
    bingoCnt = check()
    if bingoCnt>=3:
      print(a+1)
      break

