import math
def solution(n, k):
    answer = []
    tmp = [i for i in range(1, n+1)]
    
    while tmp:
        num = (k-1) // math.factorial(n-1)
        answer.append(tmp.pop(num))
        
        k = k % math.factorial(n-1)
        n -= 1
    return answer