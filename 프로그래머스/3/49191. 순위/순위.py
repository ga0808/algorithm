from pprint import pprint
def solution(n, results):
    
    graph = [([0] * n) for _ in range(n)]
    for i,j in results:
        graph[i-1][j-1] = 1

    #2번의 경기 결과들을 - 5번에도 동기화 시켜줘야함
    #바로 이어진 간선들의 연결상태 말고
    # 간접적으로 우회해서 해당 노드들에 갈 수 있는 경로가 있는지 확인해서 갱신
    for k in range(n): # k노드를 통해
        for i in range(n): # i와
            for j in range(n): # j의 우회 경로가 존재하는가 
                #i노드에서 j까지 우회노드가 존재하는데 - 0인 경우 = 경로가 없다고 되어있는 경우
                # -> 1로 경로 존재함을 표현
                #여기서 i노드에서 j노드까지 경로가 존재한다는 것의 의미
                # -> i+1 선수가 j+1선수를 이겼다
                #    = 각 i행에는 그럼 i+1번이 이긴 선수들이 1로 기록
                # -> 반대로 j+1 선수가 i+1선수에게 졌다
                #    = 각 j열에는 j+1번이 진 선수들이 1로 기록
                  if graph[i][j] == 0 and graph[i][k] ==1 and graph[k][j] ==1:
                        graph[i][j] =1
    record = [0]*n
    #i행 = i+1 선수가 이긴 선수들의 수
    #i열 = i+1 선수가 진 선수들의 수
    #i행과 i열의 합이 n-1이라면 -> i선수의 순위를 알 수 있게 됨
    for i in range(n):
        for j in range(n):
            record[i] += graph[i][j] + graph[j][i]
    answer = record.count(n-1)
    return answer