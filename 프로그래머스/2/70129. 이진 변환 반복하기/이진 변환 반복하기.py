from collections import Counter
def solution(s):
    answer = []
    cnt_zero = 0
    cnt_result = 0
    while s != "1":
        cnt_list = Counter(s)
        cnt = len(s) - cnt_list["0"]
        tmp_bin = bin(cnt)[2:]
        s = tmp_bin
        cnt_result += 1
        cnt_zero += cnt_list["0"]
    answer.append(cnt_result)
    answer.append(cnt_zero)
    return answer