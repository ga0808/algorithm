def solution(n,a,b):
#계속해서 부여받는 조 넘버가 이웃하면 -> 만나게 되는 라운드
    from math import ceil
    
    ans = 1
    a_n = ceil(a/2)
    b_n = ceil(b/2) 
    
    if abs(a_n-b_n) == 0:
        return ans
    
    while True:
        ans +=1
        if ((a_n%2) == 0) and (b_n == (a_n-1)): # 이웃하되, 2-3조 같은 경우엔 예외해야함
            return ans                          # 12  34  56 조 짝지어져서 결승해야하므로
        elif ((a_n%2)==1) and (b_n ==(a_n+1)):  # 그래서, a가 부여받은 넘버조 짝수/홀수로 경우 나눔
            return ans
        a_n = ceil(a_n/2)
        b_n = ceil(b_n/2)
