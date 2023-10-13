import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    list_ = list(input().split())
    if list_[0] == "push":
        stack.append(int(list_[-1]))
    elif list_[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif list_[0] == "size":
        print(len(stack))
    elif list_[0] == "empty":
        print(0) if len(stack) != 0 else print(1)
    elif list_[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])