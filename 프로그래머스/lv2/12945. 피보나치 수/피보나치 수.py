def solution(n): #n번째 피보나치 수를 1234567으로 나눈 나머지
    num_lst = [0,1] + [0]*(n-1)
    
    for i in range(2,n+1):
        num_lst[i] = num_lst[i-1] + num_lst[i-2]
    return num_lst[-1]%1234567