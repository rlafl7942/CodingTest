def solution(name, yearning, photo):
    answer = []
    for name_list in photo:
        tmp = 0
        for index, value in enumerate(name):
            if value in name_list:
                tmp += yearning[index]
        answer.append(tmp)
    return answer