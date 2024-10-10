def solution(k, score):
    answer = []
    process = []
    
    for index, value in enumerate(score):
        process.append(value)
        process = sorted(process, reverse=True)
        
        if len(process)<k:
            answer.append(min(process))
        else:
            
            minz = process[0]
            for i in range(0, k):
                if process[i]<minz:
                    minz=process[i]
            answer.append(minz)
    
    return answer