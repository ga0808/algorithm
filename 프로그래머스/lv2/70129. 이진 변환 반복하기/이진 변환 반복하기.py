def solution(s):
    answer = [0, 0] #2진 변환의 횟수, 제거된 0의 개수
    
    while s != "1":
        answer[1] += s.count("0")
        x = s.replace("0","")
        s = str(bin(len(x)))[2:]
        answer[0] += 1

    return answer