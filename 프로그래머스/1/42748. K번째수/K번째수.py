def solution(array, commands):
    answer = []
    for i in commands:
        start, end, order = i[0], i[1], i[2]
        tmp = array[start-1:end]
        tmp.sort()
        answer.append(tmp[order-1])
    
    return answer