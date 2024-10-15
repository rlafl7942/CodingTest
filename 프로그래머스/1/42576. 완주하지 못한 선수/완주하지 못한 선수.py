from collections import Counter
def solution(participant, completion):
    answer = ''
    cnt = Counter(participant)
    for i in completion:
        if cnt[i]:
            cnt[i]-=1
    for i in participant:
        if cnt[i] == 1:
            return i
    
    return answer