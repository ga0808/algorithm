def solution(triangle):
    #큰 문제를 풀기위한 작은 문제는 어떻게 정의할 수 있을까?
    #triangle 에 있는 값 자체를 위 노드 값들을 합치면서 변형시켜보자 !
    
        # [[7], 
        #  [3, 8], 
        #  [8, 1, 0], 
        #  [2, 7, 4, 4], 
        #  [4, 5, 2, 6, 5]]
    
    for row_idx, row in enumerate(triangle): #row = [3, 8]
        if row_idx ==0:
            continue
        #각 리스트 내에 있는 값들을 가져와서 - 이전 루트에서 max값 더하기
        for i in range(len(row)):
            #각 리스트내에 첫번째 값 -> 이전 리스트의 첫번째 값 밖에 못가져옴
            if i == 0:
                triangle[row_idx][0] += triangle[row_idx-1][0]
            #각 리스트 내에 마지막 값 -> 이전 리스트의 마지막 값 밖에 못가져옴
            elif i == len(row)-1:
                triangle[row_idx][-1] += triangle[row_idx-1][-1]
            #중간 인덱스에 있는 모든 값들 -> 이전 리스트의에서 둘중에 큰것 가져와야함
            else: 
                #현재 값의 인덱스보다 -1 인덱스 , 같은 인덱스 의 값 두개를 비교해서 가져와야함
                triangle[row_idx][i] += max( triangle[row_idx-1][i-1], triangle[row_idx-1][i])
        
    return max(triangle[-1])