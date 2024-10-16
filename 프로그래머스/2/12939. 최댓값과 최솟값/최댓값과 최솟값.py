def solution(s):
    answer = ''
    tmp = []
    for i in s.split(" "):
        tmp.append(int(i))
            
    answer += str(min(tmp))
    answer += " "
    answer += str(max(tmp))
    return answer