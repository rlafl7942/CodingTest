import sys

input = sys.stdin.readline

board = list(map(str, input().rstrip()))

cnt=0
cnt_stack = []
answer=""
for i in board:
  if i == 'X':
    cnt+=1
  else:
    if cnt!=0:
      cnt_stack.append(cnt)
    cnt_stack.append(0)
    cnt=0
if cnt!=0:
  cnt_stack.append(cnt)
  cnt=0

flag=0
for i in cnt_stack:
  if i==0:
    answer+="."
  if i%2!=0:
    print(-1)
    flag=1
    break
  if (i-4)%2==0:
    while i>=4:
      answer+="AAAA"
      i-=4
  if i%2==0:
    while i>=2:
      answer+="BB"
      i-=2

if flag==0:
  print(answer)