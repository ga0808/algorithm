

#방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문

#n : 노드 개수
#m : 간선 개수
#v : 시작할 노드 번호
n, m, v = map(int, input().split())

#다음에 주어지는 정보들은 
#노드 - 연결된 노드 의 쌍이 순차적으로 들어옴 
#우리는 두 노드가 연결되었다, 되지 않았다를 하나의 행렬=그래프로 만들고자 함 
# 엑셀-> 각 노드는 행과 열의 인덱스가 될 것이고 - 엑셀 테이블 내에는 연결(T),연결안됨(F)
#노드들의 연결 여부 정보를 통해서 우리는 방문처리를 하고, 방문 경로를 출력할 것임

#graph =    0 1 2 3 4 행
	      # 0 F F F F F
        # 1 F F T T T
        # 2 F T F F F
        # 3 F T F F F
        # 4 F T T T F
        # 열

graph = [] #빈 그래프 리스트에 - 각 노드에 대한, [노드별 연결 여부 데이터들] 리스트 추가
#여기서도 우리 0인덱스는 그냥 사용하지 않고, 없는 노드라 생각하겠음 
for _ in range(n+1): 
  #별로 의미없는 변수 같은 경우에는 그냥 _언더바 처리하기도 함 
  graph.append([False] * (n+1))

#graph = [ [],  [F,F,F...] ,  [F,F,F..]]
#             1번 노드 연결여부  2번 노드 연결여부

#모두 False로 되어있는 graph
#연결되어 있는 노드 정보들 받아와서 True로 갱신
for _ in range(m): #연결 정보는 간선이니까 - 간선의 개수 만큼 반복
    a, b = map(int, input().split())
    graph[a][b] = True
    #1-2가 연결된거면 , 2-1 관점에서 봐도 연결된 것으로 판단되어야 함
    graph[b][a] = True

visited_dfs = [False] * (n + 1)  # dfs의 방문기록

##########
visited_bfs = [False] * (n + 1)  # bfs의 방문기록

def dfs(v):
    visited_dfs[v] = True  # 해당 v값 방문처리
    print(v, end=" ")
    for i in range(1, n + 1): #가지고 있는 노드들 모두 가져오기- 0노드는 없어서 1노드 부터
        # 만약 i 노드를 아직 방문하지 않았고 +  현재 노드인 v와 연결이 되어 있다면 
        # - 해당 노드의 인접 노드들을 재귀로 더 깊이 탐색
        # i노드 방문 여부 : visited_dfs[i] -> 방문 아직 안했으면 : False
        # v-i노드 연결 여부 : graph[v][i] -> v,i연결 되어 있으면 : True
        # 두 조건이 모두 True여야 if문 실행됨 -> i노드 방문 여부 에는 not 
        if not (visited_dfs[i]) and graph[v][i]:
          dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)

##########
from collections import deque
def bfs(v):
  # pop메서드의 시간복잡도가 낮은 데크 사용
  # 시작 노드 넣은 큐(데크)생성 
  q = deque([v])  
  # 시작 노드 미리 방문처리
  visited_bfs[v] = True  

  # 노드 pop 하고 - pop한 노드의 인접노드들 모두 큐에 삽입 - 큐가 빌 때까지 반복
  #while 동작 조건으로 - 반복 가능한 객체를 넘겨주면, 값 존재하면 True 
  while q:  
      # 큐에 값 pop - 값이 뒤쪽으로 추가되어 - 맨 앞쪽(왼쪽)값 pop  
      v = q.popleft()  
      # pop한 노드 방문 경로로 출력 
      print(v, end=" ")
      #노드들 다 돌면서, 방문하지 않은 노드인지 + 인접 노드인지 체킹
      # -> 맞으면 큐에 추가 + 방문 처리 
      for i in range(1, n + 1):
          #i 방문 안했고  +  두개 연결안되어 있다면
          if not visited_bfs[i] and graph[v][i]: 
              #인접 노드 i 추가 
              q.append(i) 
              #인접 노드 i 방문 처리
              visited_bfs[i] = True 


dfs(v)
print() 
#print() 안써주면 - dfs, bfs가 한줄에 출력되어 버림 end=' '로 설정해서
#그래서 아무것도 출력안할거고, 근데 print()는 실행이되어서 한번 문장 끊어냄
bfs(v)

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4