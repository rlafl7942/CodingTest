from collections import Counter
def solution(k, tangerine):
    answer = 1
    counter = Counter(tangerine)
    cnt = sorted(list(counter.values()),reverse=True)
    basket = 0
    for i in cnt:
        basket += i
        if basket >= k:
            return answer
        answer += 1
    return answer