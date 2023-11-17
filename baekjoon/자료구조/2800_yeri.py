import sys
from itertools import combinations

# enumerate, combinations, sorted 개념 정리 필요

problem = list(input())
p, b_idx = [],[]

result = set() #중복이 생길 수도 있기 때문에 set

for i,v in enumerate(problem):
  if v == "(" :
    problem[i]=""
    p.append(i)
  
  if v == ")" :
    problem[i]=""
    b_idx.append([p.pop(),i])

for i in range(len(b_idx)):
  for j in combinations(b_idx, i):
    P = problem[:]
    for s,e in j:
      P[s]="("
      P[e]=")"
    result.add("".join(P))

print(*sorted(result),sep="\n")
