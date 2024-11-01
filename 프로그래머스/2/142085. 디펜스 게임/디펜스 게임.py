import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    for i in range(len(enemy)):
        if n >= enemy[i]:
            n -= enemy[i]
            heapq.heappush(q, (-enemy[i], enemy[i]))
        elif k > 0:
            if q and enemy[i] < q[0][1]:
                n += heapq.heappop(q)[1] - enemy[i]
                heapq.heappush(q, (-enemy[i], enemy[i]))
            k -= 1
        else:
            answer = i
            break
        answer = i + 1
    return answer