def solution(scoville, K):
    #모든 음식이 k 스코빌 이상일 때까지
    #- 두 음식의 스코빌을 섞은 음식 스코빌 지수 공식을 통해-하나의 음식으로 만들며 스코빌 지수 얻음- 반복
    #- 모두 k 이상이 되는 최소 횟수를 return
    
    import heapq
    heapq.heapify(scoville)
    #음식 섞은 횟수 
    cnt = 0
    while scoville[0] < K: #최소 스코빌 지수가 k 미만이면 계속 반복
        if len(scoville)==1:
            return -1

        min_food = heapq.heappop(scoville)
        min_food_2 = heapq.heappop(scoville)
        new_food = min_food + (min_food_2 * 2)
        heapq.heappush(scoville, new_food)
        cnt += 1
        

    return cnt