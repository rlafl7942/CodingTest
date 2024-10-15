def solution(keymap, targets):
    answer = []
    dic = dict()
    for maps in keymap:
        for index, value in enumerate(maps):
            if value in dic:
                if dic[value] > index:
                    dic[value] = index
            else:
                dic[value] = index
    for target in targets:
        cnt=0
        flag=0
        for index, value in enumerate(target):
            if value in dic:
                cnt+=dic[value]+1
            else:
                flag=1
                break
        if flag==1:
            answer.append(-1)
        else:
            answer.append(cnt)
    return answer