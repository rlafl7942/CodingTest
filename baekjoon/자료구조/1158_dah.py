import sys
input = sys.stdin.readline

n, k = map(int, input().split())

people = [_ for _ in range(1, n+1)]
p = k-1

# answer = "<"
answer = []
for _ in range(n):
    # if _ == n-1:
    #     answer += str(people.pop(p))+">"
    # else:
    #     answer += str(people.pop(p))+", "
    answer.append(people.pop(p))
    p += (k-1)
    if people and p >= len(people):
        p = p % len(people)


print("<" + ", ".join(map(str, answer)) +">")