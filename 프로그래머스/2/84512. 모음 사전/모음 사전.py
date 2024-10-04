def solution(word):
    word_list = []
    alphabet = ["A", "E", "I", "O", "U"]
    
    def dfs(word, cnt):
        if cnt==5:
            return
        
        for i in range(len(alphabet)):
            word_list.append(word+alphabet[i])
            dfs(word+alphabet[i], cnt+1)
    
    dfs("", 0)
    
    return word_list.index(word)+1