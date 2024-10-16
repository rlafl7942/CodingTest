def solution(A,B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse= True)
    
    while A and B:
        answer += A.pop() * B.pop()

    return answer