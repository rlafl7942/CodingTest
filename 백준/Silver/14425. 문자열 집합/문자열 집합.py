import sys

input = sys.stdin.readline

n, m = map(int, input().split())
st = set()
for _ in range(n):
  st.add(input().strip())

answer = 0
for _ in range(m):
  if input().strip() in st:
    answer += 1
print(answer)