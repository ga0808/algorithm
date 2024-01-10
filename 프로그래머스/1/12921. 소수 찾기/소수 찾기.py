def solution(n):
    nums=[]
    for i in range(2,n+1):
        check = 0
        for j in range(1,int(i**0.5)+1):
            if check>=2:
                break
            elif i%j ==0:
                check +=1
        if check ==1:
            nums.append(i)
    answer = len(nums)
    return answer