def solution(s, skip, index):
    answer = ''
    sk=[]
    for i in skip:
        sk.append(i)
        
    for i in s:
        tmp = ord(i)
        cnt = 0
        while cnt!=index:
            tmp+=1
            while chr((ord(chr(tmp))-ord("a"))%26+ord("a")) in sk:
                tmp += 1
            cnt += 1
        answer+=chr((ord(chr(tmp))-ord("a"))%26+ord("a"))

    return answer