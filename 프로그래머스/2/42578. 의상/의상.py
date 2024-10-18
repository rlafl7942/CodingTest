from itertools import combinations
from collections import defaultdict
def solution(clothes):
    cloth = defaultdict(list)
    for value in clothes:
        item, type = value[0], value[1]
        cloth[type].append(item)
    tmp = 1
    for i in cloth:
        tmp *= (len(cloth[i]) +1)

    return tmp-1