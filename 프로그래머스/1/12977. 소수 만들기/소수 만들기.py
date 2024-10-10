from itertools import combinations
import math
def solution(nums):
    collections = list(combinations(nums, 3))
    cnt = 0
    for i in collections:
        tmp = sum(i)
        tmp_cnt = 0
        for j in range(1, int(math.sqrt(tmp))+1):
            if tmp%j==0:
                tmp_cnt+=1
                if j*j==tmp:
                    tmp_cnt+=1
        if tmp_cnt ==1:
            cnt+=1
    return cnt
                