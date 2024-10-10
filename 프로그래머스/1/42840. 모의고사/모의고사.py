def solution(answers):
    tmp1 = [1,2,3,4,5]
    tmp2 = [2,1,2,3,2,4,2,5]
    tmp3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0, 0, 0]
    answer = []
    
    for index, value in enumerate(answers):
        if value == tmp1[index%5]:
            result[0] += 1
        if value == tmp2[index%8]:
            result[1] += 1
        if value == tmp3[index%10]:
            result[2] += 1
    
    max_score=0
    for index, value in enumerate(result):
        if max_score<value:
            max_score=value
    
    for index, value in enumerate(result):
        if max_score==value:
            answer.append(index+1)
    return sorted(answer)
        