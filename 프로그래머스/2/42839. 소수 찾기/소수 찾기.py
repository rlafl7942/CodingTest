import math
from itertools import permutations
from collections import deque
def solution(numbers):
    answer = 0
    q = deque(numbers)
    tmp = []
    for i in range(len(q)):
        t = set(permutations(q, i+1))
        tmp += t
    for i in range(len(tmp)):
        t = "".join(tmp[i])
        if t.startswith("0") or t == "1":
            continue
        else:
            cnt=0
            for j in range(1, int(math.sqrt(int(t)))+1):
                if int(t) % j == 0:
                    cnt+=1
            if cnt==1:
                answer += 1
    return answer