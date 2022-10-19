def solution(sizes):
    answer = 0
    w = 0 # 최대 가로길이
    h = 0 #최대 세로 길이
    for s in sizes:
        s.sort(reverse= True)
        if w < s[0]:
            w = s[0]
        if h < s[1]:
            h = s[1]
    answer = w*h        
    return answer