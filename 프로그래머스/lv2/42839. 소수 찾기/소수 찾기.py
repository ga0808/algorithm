def solution(numbers):
    from itertools import permutations
    answer = []
    num_lst = [ str(n) for n in numbers]
    per_lst = []
    for j in range(1,len(num_lst)+1):
        for i in permutations(num_lst,j):
            num = "".join(i)
            per_lst.append(num)
    per_lst = list(set(map(int, per_lst)))
    print("per_lst", per_lst)
    for p in per_lst:
        if p <=0 or p ==1 :
            continue
        elif p ==2:
            answer.append(p)
        else:
            for k in range(2,(p//2)+2): #for 문 다 돌았는데도 나머지가 0 아닌건 소수로 인정
                if p%k ==0:
                    break
                elif k == (p//2)+1:
                    if p%k !=0:
                        answer.append(p)
    return len(answer)