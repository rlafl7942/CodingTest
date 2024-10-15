def solution(n, lost, reserve):
    answer = 0
    student = [1 for i in range(1, n+1)]
    for i in lost:
        student[i-1] -= 1
    for i in reserve:
        student[i-1] += 1
    
    for index, value in enumerate(student):
        if value>1:
            if index-1>=0 and student[index-1]==0:
                value -= 1
                student[index-1] += 1
            elif index+1<len(student) and student[index+1]==0:
                value -= 1
                student[index+1] += 1
    for i in student:
        if i>0:
            answer+=1
    return answer