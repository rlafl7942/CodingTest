def solution(n):
    tmp = n
    cnt = 0
    while tmp!=0:
        if tmp%2:
            cnt+=1
        tmp//=2
    cnt_a = 0
    n+=1
    while True:
        tmp_a = n
        while tmp_a!=0:
            if tmp_a%2:
                cnt_a+=1
            tmp_a//=2
        if cnt_a == cnt:
            return n
        n+=1
        cnt_a = 0