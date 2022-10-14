def solution(s):
    answer = ''
    num = (len(s)-1)//2 #2  1
    
    if len(s)%2 != 0:
        answer += s[num]
    elif len(s)%2 == 0:
        answer += s[num]
        answer += s[num+1]
    
    return answer