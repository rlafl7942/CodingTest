def solution(arr):
    min_num = min(arr)
    answer=[]
    for i in arr:
        if i != min_num:
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    
    return answer