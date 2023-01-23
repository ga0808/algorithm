def solution(k, m, score):
    #k= 최상품 사과 점수
    #m= 한 상자에 담기는 사과 개수
    answer = 0
    m_lst = []
    l=m-1
    score.sort(reverse=True)
    for i in range(len(score)//m):
        m_lst.append(score[l]*m)
        l+=m
    return sum(m_lst)
    
    # else:
    #     for s in range(len(score)//m):
    #         # if len(score) < m:
    #         #     break
    #         for mm in range(m):
    #             if mm == m-1:
    #                 min_lst.append(max(score)*m)
    #                 score.remove(max(score))
    #                 break
    #             score.remove(max(score))
    #     return sum(profit)