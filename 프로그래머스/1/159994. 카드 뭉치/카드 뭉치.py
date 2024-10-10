def solution(cards1, cards2, goal):
    stack1 = []
    stack2 = []
    
    for i in range(len(cards1)-1, -1, -1):
        stack1.append(cards1[i])
        
    for i in range(len(cards2)-1, -1, -1):
        stack2.append(cards2[i])
    
    for word in goal:
        if stack1 and word == stack1[-1]:
            stack1.pop()
        elif stack2 and word == stack2[-1]:
            stack2.pop()
        else:
            return "No"
    return "Yes"