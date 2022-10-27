def solution(a, b, n):
    answer = 0
    #a개 미만일 시에는 추가적 빈병 못받음
    #a개 가져다주면 b개의 병을 줌
    #n개를 가져다주면 몇병을 받을 수 있을까?
    
    #다음단계의 콜라병= (n을 a로 나눈 몫*b) + 나머지
    #answer = 마지막 단계까지의 몫의 합
    while n>=a:
        answer += (n//a)*b
        n = ((n//a)*b) + (n%a)
        print(n)
    return answer