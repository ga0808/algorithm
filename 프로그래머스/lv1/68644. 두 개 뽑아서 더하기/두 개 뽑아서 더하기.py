def solution(numbers):
    answer = []
    num = 0
    
    for n in range(len(numbers)):
        if n != len(numbers):
            for j in range(n+1,len(numbers)):
                num = numbers[n] + numbers[j]
                if num not in answer:
                    answer.append(num)
    answer.sort()
    return answer