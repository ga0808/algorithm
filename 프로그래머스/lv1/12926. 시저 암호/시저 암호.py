def solution(s, n):
    answer = ''
    for i in range(0,len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            num = ord(s[i])
            if 65<= num <=90:
                if num+n>90:
                    num = num+n-26
                else:
                    num+=n
            elif 97<= num <=122:
                if num+n>122:
                    num = num+n-26
                else:
                    num+=n  
            
            answer += chr(num)  
    return answer 