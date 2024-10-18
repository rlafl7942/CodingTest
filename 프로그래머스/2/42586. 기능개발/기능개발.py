def solution(progresses, speeds):
    answer = []
    stack = []
    for index, value in enumerate(progresses):
        if (100 - value) % speeds[index] == 0:
            stack.append((100 - value) // speeds[index])
        else:
            stack.append((100 - value) // speeds[index] + 1)
    print(stack)
    max_cnt = stack[0]
    cnt = 1
    for index, days in enumerate(stack):
        if index ==0:
            continue
        if days > max_cnt:
            max_cnt = days
            answer.append(cnt)
            cnt=1
        else:
            cnt+=1
    answer.append(cnt)
    return answer