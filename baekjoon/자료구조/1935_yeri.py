import sys

n = int(input())
order=sys.stdin.readline().strip()
num_stack=[]
result_stack=[]

for i in range(n):
  num_stack.append(int(input()))

for i in order:
  if i >= "A" and i <="Z":
    result_stack.append(num_stack[ord(i)-ord("A")])
  else:
    a=result_stack.pop()
    b=result_stack.pop()
    
    if i=="*":
      result_stack.append(a*b)
    elif i=="+":
      result_stack.append(a+b)
    elif i=="/":
      result_stack.append(b/a)
    else:
      result_stack.append(b-a)

print("%.2f" %result_stack[0])