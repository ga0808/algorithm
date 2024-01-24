n = int( input() )
cities = list( map(int, input().split() ) )
budget = int( input())

cities.sort()

#한 지방에서 가질 수 있는 최소 값은? - 최소 청구액을 가진 해당 지방의 청구액 or 그 청구액이 버짓보다 커서, budget/지방수 해서 똑같이 분할 한 금액
start = budget//len(cities)
#한 지방에서 가질 수 있는 최대 값은? - 버짓이 무한이다 펑펑 돈이 남는다. 최대 청구액을 가진 해당 지방의 청구액
end = max(cities)

#값 탐색 하기전에 각 지방 청구액을 다 더해도 우리 예산이 더 클때 - 그냥 최대값인 end를 주면 될것
if sum(cities) <= budget:
  print(end)

else:
  while True:
    #mid 값으로 - 총 예산 계산해서 - 우리가 가진 budget과 대소 비교
    #mid = 각 지방에 주려고 하는 지원액이 됨
    mid = (start + end) //2

    #총 예산 계산
    total = 0
    for c in cities:
      if c >= mid: #지원액 보다 크면, 지원액까지 밖에 못줌
        total += mid
      else:
        total += c
      #min(c, mid)하나로 가능함

    #총 청구액이 우리가 가진 예산과 대소 비교 -> start, end 조정 해줘야함
    #총 청구액 > 예산 -> mid를 낮추기 위해 end를 더 낮춰야함
    if total > budget:
      end = mid-1
    #총 청구액 < 예산 -> mid를 높이기 위해 start를 더 높여야함
    elif total < budget:
      start = mid+1
    #총 청구액 = 예산 -> mid 출력 
    else :
      print(mid)
      break
        
    if start>end :
      print(end)
      break
