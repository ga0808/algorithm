from collections import deque

def solution(S):
    if len(set(S)) == 1 and len(S)%2==1:
        return 0
    
    remain = deque()
    
    for s in S:
        remain.append(s)
        if len(remain) == 1:
            continue
        elif remain[-2] == remain[-1]:
            remain.pop()
            remain.pop()
            
    if len(remain) == 0:
        return 1
    else :
        return 0
    