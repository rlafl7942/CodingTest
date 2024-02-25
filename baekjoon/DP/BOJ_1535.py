import sys

input = sys.stdin.readline

n = int(input())
L = [0] + list(map(int, input().split())) #체력
J = [0] + list(map(int, input().split())) #기쁨
dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1,101):
    if L[i] <= j: 
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][99])