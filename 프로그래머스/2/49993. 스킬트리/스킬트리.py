from collections import deque
def solution(skill, skill_trees):
    answer = 0
    stack = []
    for word in skill_trees:
        standard = deque(skill)
        flag=0
        for i in word:
            if i in standard:
                if i != standard[0]:
                    flag=1
                    break
                else:
                    standard.popleft()
        if flag==0:
            answer+=1
    return answer