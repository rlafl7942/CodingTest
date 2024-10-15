def solution(lottos, win_nums):
    answer = []
    cnt_same = 0
    cnt_possible = 0
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5}
    for index, value in enumerate(lottos):
        if value==0:
            cnt_possible+=1
            continue
        for j in win_nums:
            if value==j:
                cnt_same+=1
                continue
        
    if cnt_same+cnt_possible in ranking:
        answer.append(ranking[cnt_same+cnt_possible])
    else:
        answer.append(6)
        
    if cnt_same in ranking:
        answer.append(ranking[cnt_same])
    else:
        answer.append(6)
    return answer