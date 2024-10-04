from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [False for _ in range(len(words))]
    
    while q:
        word, depth = q.popleft()
        if word == target:
            return depth
        
        for i in range(len(words)):
            if not visited[i]:
                cnt = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        cnt+=1
                if cnt==1:
                    q.append((words[i], depth+1))
                    visited[i] = True
                    
    return 0