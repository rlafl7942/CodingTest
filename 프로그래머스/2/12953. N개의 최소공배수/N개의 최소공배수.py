def gcd(x, y):
        while y:
            x, y = y, x%y
        return x

def lcm(x, y):
    return abs(x*y) // gcd(x,y)

def solution(arr):
    answer = 0
    
    while len(arr)>=2:
        x = arr[0]
        y = arr[1]
        arr.append(lcm(x,y))
        arr = arr[2:]
    answer = arr[0]
    return answer