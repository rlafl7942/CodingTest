def solution(order):
    stack = []
    index = 0
    for i in range(1, len(order)+1):
        stack.append(i)
        
        while stack and stack[-1] == order[index]:
            stack.pop()
            index += 1
    return index