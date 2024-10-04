from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    n_set = []
    for i in X:
        if y[i] > 0:
            n_set.append(i)
            y[i] -= 1
            
    n_set.sort(reverse = True)
    if len(n_set)==0:
        return "-1"
    elif n_set[0] == "0":
        return "0"
    else:
        return "".join(n_set)