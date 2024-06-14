def solution(nums):
    answer = 0
    tmp = set(nums)
    if len(tmp) > len(nums)/2:
        return len(nums)/2
    else:
        return len(tmp)
