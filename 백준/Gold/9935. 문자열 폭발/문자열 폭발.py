import sys

input = sys.stdin.readline

order = input().strip()
boom = input().strip()

stack = []
for i in range(len(order)):
  stack.append(order[i])
  if "".join(stack[-len(boom):]) == boom:
    for _ in range(len(boom)):
      stack.pop()
if stack:
  print("".join(stack))
else:
  print("FRULA")