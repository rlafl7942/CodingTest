def solution(n):
    tmp = []
    while n!=0:
        tmp.append(str(n%10))
        n//=10
    tmp.sort(reverse=True)
    return int("".join(tmp))