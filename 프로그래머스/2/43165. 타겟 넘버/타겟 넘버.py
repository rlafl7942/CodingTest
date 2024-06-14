def solution(numbers, target):
    answer = 0
    tmp = [0]
    for num in numbers:
        tmp_2 = []
        for i in tmp:
            minus = i-num
            plus = i+num
            tmp_2.append(minus)
            tmp_2.append(plus)
        tmp = tmp_2
    
    for i in tmp:
        if i==target:
            answer+=1
            
    return answer
            
            
            
        