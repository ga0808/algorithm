def solution(n, left, right):
    #left의 행, 열 위치 알아내서 - 어떤 값을 가지는지 추론하기
    # 1 : 0행-0열
    # 2 : 0행-1열, 1행-0열,1열
    # 3 : 0행-2열, 1행-2열, 2행-0,1,2열
    # n : 0~n-2 행까지는 n-1열에만 숫자 n
    #       i행 => i열까지 i, 그 뒤에는 i+1씩 됨
    #     n-1 행에는 n으로 모두
    #     
    
    # 1 2 3 4 
    # 2 2 3 4 (1,3)
    # 3 3 3 4 (2,0)
    # 4 4 4 4 (3,2)
    nums = []
    for i in range(left,right+1):
        row_idx = i // n
        col_idx = (i % n)          
        # print(i,row_idx,col_idx)
        if row_idx == 0:
            nums.append(col_idx+1)
        elif (row_idx == n-1) or (col_idx == n-1):
            nums.append(n)
        else:
            #i행 => i열까지 i, 그 뒤에는 i+1씩 됨
            j = row_idx - col_idx
            if j >= 0:
                # print(j,i,row_idx,col_idx,">="*10)
                nums.append(row_idx+1)
            else:
                # print(j,i,row_idx,col_idx,"<"*10)
                nums.append(col_idx+1)
                
    return nums