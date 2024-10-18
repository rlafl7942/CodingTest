from collections import Counter
def solution(str1, str2):
    answer = 0
    arr1 = []
    arr2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) == 0 and len(str2) == 0:
        return 65536
    
    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            arr1.append((str1[i]+str1[i+1]).lower())
    for i in range(len(str2)-1):
        if (str2[i] + str2[i+1]).isalpha():
            arr2.append((str2[i]+str2[i+1]).lower())
    
    cnt1 = Counter(arr1)
    cnt2 = Counter(arr2)
    together = []
    plus = []
    for i in cnt1:
        if i in cnt2:
            for _ in range(min(cnt1[i], cnt2[i])):
                together.append(i)
            for _ in range(max(cnt1[i],cnt2[i])):
                plus.append(i)
        else:
            for _ in range(cnt1[i]):
                plus.append(i)
    for i in cnt2:
        if i not in cnt1:
            for _ in range(cnt2[i]):
                plus.append(i)
    if len(together) == 0 and len(plus) == 0:
        return 65536
    else:
        return int(len(together)/len(plus) * 65536)
    return answer