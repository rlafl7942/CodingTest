def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for column in board:
            if column[i-1] != 0:
                stack.append(column[i-1])
                column[i-1]=0
                break
        if len(stack)>1:
            if stack[-1] == stack[-2]:
                answer+=2
                stack.pop()
                stack.pop()
    return answer