import sys

word = list(sys.stdin.readline().strip())

answer=0
stack=[]
tmp_answer=1


for i in range(len(word)):
  if word[i]=="(":
    stack.append(word[i])
    tmp_answer*=2

  elif word[i]=="[":
    stack.append(word[i])
    tmp_answer*=3
  
  elif word[i]==")":
    if len(stack)==0 or stack[-1]=="[":
      answer=0
      break
    else:
      if word[i-1]=="(":
        answer+=tmp_answer
      stack.pop()
      tmp_answer//=2

  elif word[i]=="]":
    if not stack or stack[-1]=="(":
      answer=0
      break
    else:
      if word[i-1]=="[":
        answer+=tmp_answer
      stack.pop()
      tmp_answer//=3


print(answer)




