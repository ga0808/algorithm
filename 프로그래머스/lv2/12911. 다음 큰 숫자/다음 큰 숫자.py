def solution(n):
    k = n+1
    while True:
        res = True
        #one_cnt = bin(n)[2:].count('1')
        if bin(n)[2:].count('1') == bin(k)[2:].count('1'):
            return k
        k+=1