import sys

input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

count = [0] * (max(numbers)+1) # 숫자 몇 번 나왔는지 세기
max_length = 0
left = 0
right = 0
while True:
  if right >= n:
    break
  if count[numbers[right]] < k: # 숫자가 k번 나오지 않았다면
    count[numbers[right]] += 1 # 1씩 증가
    right += 1
  else: # 숫자가 k번 이상 나오면
  # 지금까지 말고 더 뒤에 최장 연속 수열 있을수도 있으니
  # 해당 숫자의 count -= 1, left += 1 처리
    count[numbers[left]] -= 1 
    left += 1
  max_length = max(max_length, right-left) # 길이 갱신
print(max_length)
