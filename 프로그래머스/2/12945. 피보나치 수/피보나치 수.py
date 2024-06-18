def solution(n):
    a = 1
    b = 1
    tmp = 0
    if n == 2:
        return 1%1234567
    for i in range(3, n+1):
        tmp = a+b
        a = b
        b = tmp
    return(tmp%1234567)