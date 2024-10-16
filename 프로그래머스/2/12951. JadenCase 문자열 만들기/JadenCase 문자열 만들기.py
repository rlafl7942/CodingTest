def solution(s):
    answer = ''
    tmp = s.split(" ")
    
    for word in tmp:
        for index, alphabet in enumerate(word):
            if index == 0:
                if alphabet.isnumeric() or alphabet == " ":
                    answer += alphabet
                else:
                    if alphabet.islower():
                        answer += alphabet.upper()
                    else:
                        answer += alphabet
            else:
                if alphabet.isupper():
                    answer += alphabet.lower()
                else:
                    answer+=alphabet
        answer += " "
    return answer[:-1]