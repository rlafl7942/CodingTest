from collections import Counter
def solution(topping):
    answer = 0
    dic = Counter(topping)
    topping_set = set()
    
    for i in topping:
        dic[i] -= 1
        topping_set.add(i)

        if dic[i] ==0:
            dic.pop(i)
        
        if len(topping_set) == len(dic):
            answer+=1
    return answer