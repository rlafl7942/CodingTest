from collections import deque
def lcm(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def solution(arrayA, arrayB):
    answer = 0
    q = deque(arrayA)
    while len(q)>1:
        a = q.popleft()
        b = q.popleft()
        q.append(lcm(a,b))
    a_num = q[0]
    
    q = deque(arrayB)
    while len(q)>1:
        a = q.popleft()
        b = q.popleft()
        q.append(lcm(a,b))
    b_num = q[0]
    tmp = []
    if a_num != 1:
        flag = 0
        for i in arrayB:
            if i%a_num == 0:
                flag = 1
                break
        if flag == 0:
            tmp.append(a_num)
    if b_num != 1:
        flag = 0
        for i in arrayA:
            if i%b_num == 0:
                flag = 1
                break
        if flag == 0:
            tmp.append(b_num)
    if not tmp:
        return 0
    else:
        return max(tmp)
