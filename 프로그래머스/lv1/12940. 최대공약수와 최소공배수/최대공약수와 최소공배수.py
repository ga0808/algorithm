def solution(n, m):
    answer = []
    #각 수의 공약수
    n_lst = [ i for i in range(1,n+1) if n%i ==0]
    m_lst = [ i for i in range(1,m+1) if m%i ==0]
    #최대공약수
    inter = list(set(n_lst) & set(m_lst))
    answer.append(max(inter))
    print(answer)
    answer.append(n*m/max(inter))
    
    return answer