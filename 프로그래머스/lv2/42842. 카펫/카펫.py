def solution(brown, yellow):
    answer = []
    # brown + yellow = (카펫 가로 * 카펫 세로)
    square = brown+yellow
    for width in range(square-1,2,-1):
        if ((width-2)*((square//width) -2) == yellow):
            answer = [width, square// width]
            break
    return answer