# 01
# import sys
# input = sys.stdin.readline


# n = int(input())
# for _ in range(n):
#     stack = []
#     for c in list(input().rstrip()):
#         if c == '(':
#             stack.append(c)
#         else:
#             if len(stack) == 0:
#                 stack.append('*')
#                 print("NO")
#                 break
#             else:
#                 stack.pop()
#     if len(stack) != 0 and stack[0] == '*':
#         continue
#     print("YES") if len(stack) == 0 else print("NO")

# 02
import sys
input = sys.stdin.readline


n = int(input())
for _ in range(n):
    input_ = input().rstrip()

    while '()' in input_:
        input_ = input_.replace('()', '')

    print(input_)
    print("NO") if input_ else print("YES")