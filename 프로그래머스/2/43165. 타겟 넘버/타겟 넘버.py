def solution(numbers, target):
    result = [[] for _ in range(len(numbers))]
    
    result[0].append(0+numbers[0])
    result[0].append(0-numbers[0])
    for i in range(1, len(numbers)):
        for j in range(len(result[i-1])):
            result[i].append(result[i-1][j]+numbers[i])
            result[i].append(result[i-1][j]-numbers[i])
    
    cnt=0
    for i in result[len(result)-1]:
        if i==target:
            cnt+=1
            
    return cnt