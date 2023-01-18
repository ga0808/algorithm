def solution(food):
    answer=""
    for i in range(1,len(food)):
    #food의 인덱스 숫자를 food 값 만큼 answer에 추가
    # 단 2로 나눈 몫 *2 만큼
        n = (food[i]//2)*2
        
        s = list(answer)
        s.insert(len(s)//2, str(i)*n)
        answer = "".join(s)

    answer = answer[:int(len(answer)//2)] +"0"+answer[int(len(answer)//2):]
    return answer