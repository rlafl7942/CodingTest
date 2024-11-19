import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
result = []

A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = A + B
c.sort()
print(*c)
# A = sorted(A)
# B = sorted(B)
# A = deque(A)
# B = deque(B)

# while A and B:
#   if A[0] < B[0]:
#     result.append(A[0])
#     A.popleft()
#   elif A[0] > B[0]:
#     result.append(B[0])
#     B.popleft()
#   else:
#     result.append(A[0])
#     A.popleft()
#     B.popleft()

# if A:
#   result += A
# if B:
#   result += B

# for num in result:
#   print(num, end =" ")