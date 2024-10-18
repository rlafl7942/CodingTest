from itertools import permutations
def solution(k, dungeons):
    answer = -1
    methods = list(permutations(dungeons, len(dungeons)))
    for method in methods:
        tmp = k
        cnt = 0
        for info in method:
            if info[0] <= tmp:
                tmp -= info[1]
                cnt += 1
        if tmp>=0:
            answer = max(answer, cnt)
        
    return answer