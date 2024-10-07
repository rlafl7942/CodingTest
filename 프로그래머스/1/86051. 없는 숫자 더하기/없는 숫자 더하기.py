def solution(numbers):
    tmp = 0
    for i in range(10):
        tmp+=i
    
    return tmp - sum(numbers)