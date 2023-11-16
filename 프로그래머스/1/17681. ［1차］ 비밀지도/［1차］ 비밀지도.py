def solution(n, arr1, arr2):
    answer_arr = []
    
    for i in range(n):
        num1 = arr1[i]
        num1_lst = []
        
        num2 = arr2[i]
        num2_lst = []
        
        while True:    
            num1_lst.append(num1 % 2)
            num1 = num1 // 2
            
            if num1 == 1:
                num1_lst.append(1)
                break
            elif num1 == 0:
                break
        
        num1_lst.reverse()
        num1_lst = [str(k) for k in num1_lst]
        num1_str = "".join(num1_lst)
        if n > len(num1_str):
            num1_str = ('0'*(n-len(num1_str))) + num1_str
        
        
        while True: 
            num2_lst.append(num2 % 2)
            num2 = num2 // 2
            
            if num2 == 1:
                num2_lst.append(1)
                break
            elif num2 == 0:
                break
                
        num2_lst.reverse()
        num2_lst = [str(k) for k in num2_lst]
        num2_str = "".join(num2_lst)
        if n > len(num2_str):
            num2_str = ('0'*(n-len(num2_str))) + num2_str

        answer = ""
        for j in range(n):
                        if num1_str[j] == "0" and num2_str[j] == "0" :
                            answer += " "
                        else:
                            answer += "#"
        answer_arr.append(answer)
    return answer_arr