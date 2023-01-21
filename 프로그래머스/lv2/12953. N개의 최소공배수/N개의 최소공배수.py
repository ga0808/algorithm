def solution(arr):
    answer = 0
    
    n=1
    while True: #다 나누어떨어지는 arr 최대값의 배수 찾기
        num = max(arr) *n 
        result = True
        #num이 arr의 모든 수로 나누어 떨어지는지 체
        #중간에 나누어 떨어지지 않는 수 있으면 for문 멈추고 num *n
        for a in arr:
            if num%a !=0:
                result=False
                break

        #num이 모든 수로 다 나누어 떨어지면 num return
        if result==True:
            break
        n +=1
    return num

