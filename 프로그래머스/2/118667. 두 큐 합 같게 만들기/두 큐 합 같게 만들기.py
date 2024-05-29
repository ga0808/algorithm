from collections import deque
import copy

def solution(q1, q2):
    ##두 큐의 각 합 구하고
    q1_sum = sum(q1)
    q1_len = len(q1)
    q2_sum = sum(q2)
    
    if q1_sum == q2_sum:
        return 0
    
    mid = (q1_sum + q2_sum)//2
    if (q1_sum + q2_sum)%2 !=0:
        return -1
    
    #1. 1/2 값 초과 값이 있으면 불가
    for i in q1+q2:
        if i > mid:
            return -1
        
    #2. 1/2값 있으면, 0부터 1/2값 인덱스 까지 다른 큐로 옮기고
    #  다시 옮긴 큐에서 0부터 1/2값 이전 인덱스까지 다른 큐로 옮김
    if mid in q1:
        #mid까지의 값
        return q1.index(mid)+1 + len(q2) + q1.index(mid)
    elif mid in q2:
        return q2.index(mid)+1 + len(q1) + q2.index(mid)
        
    #3.  더 큰애 원소를 pop&insert 계속하기
    ans = 0
    q1 = deque(q1)
    q2 = deque(q2)
    # origin_q2 = copy.deepcopy(q2)
    
    while True:
        if q1_len * 8 <ans:
            return -1
        # if q2 == origin_q2:
        #     return -1
        # if len(q1) ==1 and q1_sum > q2_sum:
        #     return -1
        # elif len(q2) ==1 and q1_sum < q2_sum:
        #     return -1
        

        if q1_sum == q2_sum:
            return ans
        elif q1_sum < q2_sum:
            pop_num = q2.popleft()
            q1.append(pop_num)
            ans+=1
            q2_sum -= pop_num
            q1_sum += pop_num
        else: # q1_sum > q2_sum:
            pop_num = q1.popleft()
            q2.append(pop_num)
            ans+=1
            q1_sum -= pop_num
            q2_sum += pop_num
    