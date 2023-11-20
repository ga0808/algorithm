def solution(triangle):
    for row_idx, row in enumerate(triangle): # 0 ,7
        if row_idx == 0:
            continue
        for i in range(len(row)):
            if i == 0:
                triangle[row_idx][0] += triangle[row_idx-1][0]
            elif i == len(row)-1:
                triangle[row_idx][-1] += triangle[row_idx-1][-1]
            else:
                triangle[row_idx][i] += max(triangle[row_idx-1][i-1], triangle[row_idx-1][i])
    
    return max(triangle[-1])
