def solution(n, arr1, arr2):
    map1 = [[0 for _ in range(n)] for _ in range(n)]
    map2 = [[0 for _ in range(n)] for _ in range(n)]
    answer = [[" " for _ in range(n)] for _ in range(n)]
    result = []
    
    for index, value in enumerate(arr1):
        tmp1 = str(format(arr1[index], "b"))
        tmp2 = str(format(arr2[index], "b"))
        
        if len(tmp1) != n:
            for i in range(len(tmp1)-1, -1, -1):
                if tmp1[i] == "1":
                    map1[index][i+(n-len(tmp1))]="#"
        else:
            for i in range(len(tmp1)-1, -1, -1):
                if tmp1[i] == "1":
                    map1[index][i]="#"    
                    
        
        if len(tmp2) != n:
            for i in range(len(tmp2)-1, -1, -1):
                if tmp2[i] == "1":
                    map2[index][i+(n-len(tmp2))]="#"
        else:
            for i in range(len(tmp2)-1, -1, -1):
                if tmp2[i] == "1":
                    map2[index][i]="#"  
                           
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == "#" and map2[i][j] == "#":
                answer[i][j] = "#"
            elif map1[i][j] != map2[i][j]:
                answer[i][j] = "#"
        
        tmp = ""
        for j in answer[i]:
            tmp += j
        result.append(tmp)
    return (result)
        
    