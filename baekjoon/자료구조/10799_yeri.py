import sys

word = list(sys.stdin.readline().strip())

stack=[]
cnt=0

for i in range(len(word)):
  if word[i]=="(":
    stack.append(word[i])
  else:
    if word[i-1]=="(":
      stack.pop()
      cnt+=len(stack)
    else:
      cnt+=1
      stack.pop()

print(cnt)