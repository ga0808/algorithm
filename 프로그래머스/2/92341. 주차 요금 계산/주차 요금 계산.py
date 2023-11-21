import math
def solution(fees, records):
    answer = []
    tmp= []
    
    for i in records:
        if len(tmp) == 0 :
            if i[0] == "0":
                    t = (60*int(i[1])) + int(i[3:5])
            else:
                t = (60*int(i[:2])) + int(i[3:5])
            tmp.append([i[6:10], t])
            continue
        
        chk = 0
        for j in tmp:
            if i[6:10] in j: #이미 차 넘버 리스트가 있을 경우
                if i[0] == "0":
                    t = (60*int(i[1])) + int(i[3:5])
                else:
                    t = (60*int(i[:2])) + int(i[3:5])
                j.append(t)
                chk = 1
        
        if chk == 0:
            if i[0] == "0":
                t = (60*int(i[1])) + int(i[3:5])
            else:
                t = (60*int(i[:2])) + int(i[3:5])
            tmp.append([i[6:10], t])
    
    fin_time = (23*60) + 59
    dict = {}

    for k in tmp:
        park_time = 0
        if len(k) % 2 == 0 :
            k.append(fin_time)
        for idx, l in enumerate(k[1:]):
            ent = 0
            exit = 0
            if idx % 2 == 0: #짝수 -> 입기록, 홀수 -> 출기록
                ent = l
            else:
                exit = l
            park_time += exit - ent

        if park_time <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil( (park_time-fees[0]) / fees[2] )*fees[-1]
        dict[k[0]] = int(fee)
        
    #차량 번호가 작은 자동차부터 청구
    dict = sorted(dict.items())
    for d in dict:
        answer.append(d[1])    
    return answer