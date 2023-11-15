def solution(wallpaper):
    # 가장 행 인덱스가 낮은=처음 발견된 #의 행 위치 값 -> 시작점의 x좌표
    # 가장 열 인덱스가 낮은=좌측의 #의 열 위치 값 -> 시작점의 y 좌표
    # 가장 행 인덱스가 높은=마지막 발견된 #의 행 위치값 +1 -> 끝점의 x좌표
    # 가장 열 인덱스가 높은=가장 우측의 #의 열 위치값 +1 -> 끝점의 y좌표
    
    s_x = -1
    s_y = -1
    e_x = -1
    e_y = -1
    
    for r_idx, row in enumerate(wallpaper):
        if row.find("#") == -1: # #이 없는 행
            continue
        else:
            if s_x == -1 : #첫번째 업데이트
                s_x = r_idx
                e_x = r_idx
                s_y = row.find("#")
                e_y = row.rfind("#") 
                print(s_x , s_y+1 , e_x , e_y+1)
        
            if s_y > row.find("#") : 
                s_y = row.find("#") 
            
            if e_x < r_idx :
                e_x = r_idx
                
            if e_y < row.rfind("#") :
                e_y = row.rfind("#") 
    
    return [s_x , s_y , e_x+1 , e_y+1]