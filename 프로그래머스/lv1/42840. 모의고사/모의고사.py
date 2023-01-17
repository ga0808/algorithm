def solution(answers):
    answer = []
    res = { 1: 0, 2:0, 3:0}   
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for a in range(len(answers)):
        if answers[a] == one[a%len(one)]:
            res[1] +=1
        if answers[a] == two[a%len(two)]:
            res[2] +=1
        if answers[a] == three[a%len(three)]:
            res[3] +=1
    answer = [k for k,v in res.items() if max(res.values()) == v]
    return answer