def solution(seoul):
    n = 0
    for i in range(0,len(seoul)):
        if seoul[i] == 'Kim':
            n = i
    answer = '김서방은 {}에 있다'.format(n)
    return answer