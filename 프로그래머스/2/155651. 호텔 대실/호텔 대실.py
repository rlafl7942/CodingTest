def solution(book_time):
    answer = 0
    book_time = sorted(book_time, key=lambda x:x[0])
    rooms = []
    for book in book_time:
        s_hour, s_minute = book[0].split(":")[0], book[0].split(":")[1]
        e_hour, e_minute = book[1].split(":")[0], book[1].split(":")[1]
        start = int(s_hour) * 60 + int(s_minute)
        end = int(e_hour) * 60 + int(e_minute) + 10 # 정리시간
        if len(rooms) < 1:
            rooms.append(end)
        else:
            flag = 0
            for index, value in enumerate(rooms):
                if start >= value:
                    rooms[index] = end
                    flag = 1
                    break
            if flag == 0:
                rooms.append(end)
                
    return len(rooms)