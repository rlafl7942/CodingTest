from collections import defaultdict
def solution(clothes):
    answer = 0
    cloth = defaultdict(int)
    for value in clothes:
        cloth[value[1]] += 1
    tmp = 1
    for value in cloth:
        tmp *= (cloth[value]+1)

    return tmp-1