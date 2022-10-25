stages = [2, 1, 2, 6, 2, 4, 3, 3]
n=5

def solution(n, stages):
    # N = 전체 스테이지의 개수
    # stages = 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열
    answer = []
    fail_dict={} #키= 스테이지, 값= 실패율
    #stages.sort()
    fail = 0
    k = 0 #스테이지 실패자 누적 값
    
    #1번 스테이지 세서 -> 남아있는 사람수/도전자수
    #n+1까지 진행

    for i in range(1,n+1):
        #도전자수 = 참가자수 - 누적된 스테이지 실패자
        try_num = len(stages) - k #해당 스테이지 도전자
        #print(try_num)
        fail_num = stages.count(i) #해당 스테이지 실패자
        k += fail_num
        #print(fail_num)

        #실패율 <- for은 스테이지 마다 리셋
        if try_num ==0:
            fail = 0
        elif try_num !=0:
            fail = fail_num/try_num
        fail_dict[i] = fail
        #print(fail_dict)
        
        #키 값을 기준으로 fail_dict 정렬
        #sorted(딕셔너리의 키/값 모두 가져와, 옵션1: xey: 어떤걸 기준으로 정렬할거야, 옵션2: 오름/내림 차순 )
        sorted_fail_dict = sorted(fail_dict.items(), key = lambda x: x[1], reverse =True )
        #print(sorted_fail_dict)
        #정렬한 딕셔너리의 키 값 -> answer에 순서대로 담기
        answer = [k[0] for k in sorted_fail_dict]
        
    return answer # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열

solution(n, stages)

# {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
# {1: 0.125, 2: 0.42857142857142855, 3: 0.4, 4: 0.16666666666666666, 5: 0.0}