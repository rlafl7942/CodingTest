def solution(n,a,b):
    answer = 1

    while True:
        if abs(a-b)==1 and min(a,b) % 2==1:
            break
        if a%2 !=0:
            a+=1
        if b%2 !=0:
            b+=1
        a//=2
        b//=2
        answer += 1
        
    return answer