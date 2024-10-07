def solution(x):
    x_sum = 0
    tmp = x
    while x!=0:
        x_sum += x%10
        x //= 10
    if tmp%x_sum ==0:
        return True
    else:
        return False