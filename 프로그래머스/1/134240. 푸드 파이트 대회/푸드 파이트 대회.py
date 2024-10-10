def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i)*(food[i]//2)
    answer += "0"
    for i in range(len(food)-1, 0, -1):
        answer += str(i)*(food[i]//2)
    return answer