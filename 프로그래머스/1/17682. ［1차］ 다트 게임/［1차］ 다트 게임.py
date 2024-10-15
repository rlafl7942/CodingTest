def solution(dartResult):
    answer = 0
    stack = []
    for index, i in enumerate(dartResult):
        if i.isnumeric():
            if i=="0":
                if index>0 and dartResult[index-1]=="1":
                    stack.pop()
                    stack.append(10)
                else:
                    stack.append(int(i))
            else:
                stack.append(int(i))
        else:
            if i=="D":
                tmp = stack.pop()
                stack.append(tmp*tmp)
            elif i=="T":
                tmp = stack.pop()
                stack.append(tmp*tmp*tmp)
            elif i=="*":
                if len(stack)==1:
                    tmp = stack.pop()
                    tmp *= 2
                    stack.append(tmp)
                else:
                    tmp1 = stack.pop()
                    tmp2 = stack.pop()
                    tmp1 *= 2
                    tmp2 *= 2
                    stack.append(tmp2)
                    stack.append(tmp1)
            elif i=="#":
                tmp = stack.pop()
                tmp *= -1
                stack.append(tmp)
    print(stack)
    return sum(stack)