import sys

n = int(input())

stack=[]
result=[]
order_num=1

for i in range(n):
  num=int(input())
  
  while num>=order_num:
    stack.append(order_num)
    result.append("+")
    order_num+=1
  
  if num==stack[-1]:
    result.append("-")
    stack.pop()


if len(stack)>0:
  print("NO")

else:
  for i in result:
    print(i)