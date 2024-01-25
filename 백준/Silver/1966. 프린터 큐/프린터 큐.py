from collections import deque

test_case = int(input())

for i in range(test_case):
  #n : 문서의 개수
  #m : 출력되는 순위를 알고 싶은 문서의 현재 인덱스 
  n , m = map(int, input().split())
  #map() : map 객체에 있는 값을 그냥 각 변수로 받아올 수 있음
  #        --> 반환받는 map 객체가 반복가능한 객체라서 변수 여러개에 저장하는 언패킹이 가능

  #우선순위
  priority = deque( map(int, input().split()) )
  #출력 회수
  cnt = 0

  while True:
    #가장 먼저 출력되어야 하는 문서 = 우선순위가 가장 큰 문서
    best = max(priority)

    #지금 프린트를 하려고 하는 문서 -> 저장해놓고 -> best와 비교해서 -> best가 맞으면 프린트,아니면 뒤로 보내기
    front = priority.popleft()

    #큐에 있던 첫번째 문서 뺐으니까 - 우리가 찾고자하는 문서의 인덱스도 -1 이됨 
    m -= 1

    if best == front: #뽑은 문서의 우선순위가 우리가 가진 문서들의 우선순위중 가장 큰 것이었는가 -> 프린트 (빼는거 맞음 - pop맞음)
       cnt +=1 #출력 횟수 +1
       if m < 0: #우리의 문서의 인덱스가 음수? : ㅡ문서가 우선순위에서 뽑혔다는 것
          print(cnt)
          break
    else: #우선순위가 아닌데 뽑혔다? - 다시 뒤로 넘겨줘야지
      priority.append(front)
      if m < 0: #뽑힌 front가 우리의 문서라면? - m(인덱스)값도 변경
         m = len(priority) - 1 #제일 뒤로 이동