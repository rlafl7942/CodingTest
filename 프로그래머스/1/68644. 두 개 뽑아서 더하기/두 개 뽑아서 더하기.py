from itertools import combinations
def solution(numbers):
    tmp = []
    for i in combinations(numbers,2):
        tmp.append(sum(i))
    answer = list(set(tmp))
    
    return sorted(answer)