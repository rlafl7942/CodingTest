def solution(k, m, score):
    score = sorted(score, reverse=True)
    answer = 0
    index = 0
            
    while index + m <= len(score):
        answer += min(score[index:index+m]) * m
        index += m
    
    return answer