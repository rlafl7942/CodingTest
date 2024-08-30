def solution(progresses, speeds):
    stack=[]
    answer=[]
    for i in range(0, len(progresses)):
        days=0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            days+=1
        stack.append(days)
        
    maxCnt = stack[0]
    print(stack)
    cnt=1
    for i in range(1, len(stack)):
        if stack[i] > maxCnt:
            maxCnt = stack[i]
            answer.append(cnt)
            cnt=1
        else:
            cnt+=1
    answer.append(cnt)
    return answer