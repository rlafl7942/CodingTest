def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9): #0-4
        flag=0
        tmp={}
        number_tmp = number.copy()
        for j in range(0,10): #0-9
            if discount[i+j] in tmp:
                tmp[discount[i+j]]+=1
            else:
                tmp[discount[i+j]]=1
        for k in range(len(want)):
            if want[k] in tmp:
                number_tmp[k]-=tmp[want[k]]
                if number_tmp[k]<0:
                    number_tmp[k]=0
                elif number_tmp[k]>0:
                    flag=1
                    break
        if flag==0:
            if sum(number_tmp)==0:
                answer+=1
    return answer