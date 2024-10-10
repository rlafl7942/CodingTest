import math
def solution(number, limit, power):
    knights = 0
    
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(math.sqrt(i))+1):
            if i%j == 0:
                cnt+=1
                if j*j != i:
                    cnt+=1
            if cnt>limit:
                break

        if cnt>limit:
            knights+=power
        else:
            knights+=cnt
    return knights
    
    