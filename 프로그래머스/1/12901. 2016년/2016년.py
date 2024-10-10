def solution(a, b): # 윤년, 2월 29일까지 있음
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    month_info = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    tmp = 5+b
    
    for i in range(a-1):
        tmp += month_info[i]
    
    return days[(tmp%7)-1]