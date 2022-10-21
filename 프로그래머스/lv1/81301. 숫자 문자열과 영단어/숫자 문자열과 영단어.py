def solution(s):
    answer= ''
    num= ''
    num_alpha = ["zero", 'one', "two", "three", "four", "five", "six", "seven", "eight","nine"]
    num_lst = ["0","1","2","3","4","5","6","7","8","9"]
    
    for i in range(len(s)):
        if s[i] not in num_lst:
            num += s[i]
            for j in range(len(num_alpha)):
                if num == num_alpha[j]:
                    answer += str(j)
                    num = ''
            
        elif s[i] in num_lst:
            answer += s[i]
    return int(answer)
            
            
            
    
    