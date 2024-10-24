from collections import defaultdict
def solution(weights):
    answer = 0
    # 가능 비율 1:1, 1:2, 2:3, 3:4
    
    dict = defaultdict(int)
    
    for w in weights:
        answer += dict[w] + dict[w*2] + dict[w/2] + dict[(w*2)/3] + dict[(w*3)/2] + dict[(w*3)/4] + dict[(w*4)/3]
        dict[w] += 1
    print(dict)
    return answer