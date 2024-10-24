def solution(sequence, k):
    answer = []
    sequence += [0]
    total = sequence[0]
    start = 0
    end = 0
    min_len = 1000000
    while end < len(sequence)-1:
        if total < k:
            end += 1
            total += sequence[end]
        elif total > k:
            total -= sequence[start]
            start += 1
        else:
            if min_len > end-start:
                min_len = end-start
                if answer:
                    answer.pop()
                answer.append((start, end))
            end += 1
            total += sequence[end]
    return answer[0]