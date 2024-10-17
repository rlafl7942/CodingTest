from collections import deque
def solution(s):
    answer = 0
    q = deque(s)
    stack = []
    for _ in range(0, len(s)):
        q.rotate(-1)
        flag = 0
        for j in q:
            if flag == 1:
                break
            if j == "[" or j=="{" or j=="(":
                stack.append(j)
            else:
                if not stack:
                    flag = 1
                    break
                else:
                    if j == "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            flag = 1
                            break
                    elif j == "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            flag = 1
                            break
                    elif j ==")":
                        if stack[-1] == "(":
                            stack.pop()
        if flag == 0 and len(stack) == 0:
            answer += 1
    return answer