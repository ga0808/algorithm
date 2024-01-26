import heapq 

def solution(scoville, K):
    #모든 음식이 k스코빌 이상일 때까지
    #- 두 음식의 스코빌을 섞음 음식 (섞은 음식 스코빌 지수 공식)을 통해서
    #  하나의 음식으로 만들며 스코빌 지수를 얻음 -> 반복
    #-return 하고 싶은것은? 모두 k지수 이상 만드는데 드는 최소 횟수
    
    heapq.heapify(scoville)
    #음식 섞은 횟수
    cnt = 0
    
    while scoville[0]<K: #가장 낮은 스코빌 지수가 k미만이면 계속 반복
        if len(scoville) == 1:
            return -1
        min_food = heapq.heappop(scoville)
        min_food_2 = heapq.heappop(scoville)
        new_food = min_food + (min_food_2*2)
        heapq.heappush(scoville, new_food)
        cnt+=1
    return cnt