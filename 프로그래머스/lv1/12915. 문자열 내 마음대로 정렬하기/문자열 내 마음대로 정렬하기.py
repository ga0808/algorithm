def solution(strings, n):
    answer = []
    s_lst = []
    for s in strings:
        s_lst.append([s[n], s])
    s_lst.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(s_lst)):
        answer.append(s_lst[i][1])
    return answer