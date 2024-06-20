def solution(brown, yellow):
    answer = []
    i=1
    while True:
        j = 0
        while i>=j:
            j+=1
            if i*j == brown+yellow:
                if (i-2) * (j-2) == yellow:
                    break
        if i>=j:
            return i,j
        i+=1
        