import sys

num = int(input())
stack = []

for i in range(num):
  flag=0
  stack=[]
  ps = list(sys.stdin.readline().strip())
  for j in range(len(ps)):
    if ps[j]=="(":
      stack.append(ps[j])
    else:
      if len(stack)>0:
        stack.pop()
      else:
        flag=1

  if flag==1 or len(stack)>0:
    print("NO")
  else:
    print("YES")
    
    

