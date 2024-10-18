def solution(s):
    answer = []
    stack = []
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key = lambda x: len(x))
    tmp = []
    for i in s:
        tmp.append(i.split(","))
    for i in tmp:
        for value in i:
            if int(value) not in stack:
                stack.append(int(value))
            
    return stack