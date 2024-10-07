from collections import Counter
def solution(s):
    cnt_list = Counter(s)
    if cnt_list["p"] + cnt_list["P"] == cnt_list["y"] + cnt_list["Y"]:
        return True
    else:
        return False
    