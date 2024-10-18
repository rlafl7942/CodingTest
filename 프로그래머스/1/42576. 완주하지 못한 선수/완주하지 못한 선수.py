from collections import Counter
def solution(participant, completion):
    answer = ''
    cnt = Counter(participant)
    for person in completion:
        cnt[person] -= 1
        if cnt[person] == 0:
            cnt.pop(person)
    for i in cnt:
        answer += i
    return answer