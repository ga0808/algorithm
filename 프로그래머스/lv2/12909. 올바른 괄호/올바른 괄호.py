def solution(s):
    answer = True
    cnt =0
    for i in range(len(s)):
        if s[i] == ')':
            cnt -=1
            if cnt < 0:
                return False
        elif s[i] == '(':
            cnt +=1
        
    if cnt != 0:
        return False

    return answer