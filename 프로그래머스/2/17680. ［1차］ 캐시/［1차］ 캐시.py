from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque(maxlen = cacheSize)
    for city in cities:
        if city.lower() not in q:
            q.append(city.lower())
            answer += 5
        else:
            q.remove(city.lower())
            q.append(city.lower())
            answer += 1
    return answer