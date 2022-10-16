n = int(input())
n_lst =list(map(int,input().split()))
# [4, 1, 5, 2, 3]

m = int(input())
m_lst = list(map(int,input().split()))
# [1, 3, 7, 9, 5]

#이진탐색 
#정렬된 리스트로 만든 후에 -> 이진 탐색
n_lst.sort()

#바이너리 타겟 값 하나 주어지면 -> 서치해서 -> T F
def b_s(target, n_lst):
    start = 0
    end = len(n_lst)-1

    while start <= end:
        mid = (start+end)//2

        if target > n_lst[mid]:
            start = mid+1
        elif target < n_lst[mid]:
            end = mid-1
        elif target == n_lst[mid] :
            return 1
    return 0

       
#타겟 값 for 문 또는 while 문으로 하나씩 b_S 함수 실행
for i in range(0,len(m_lst)):
    result= b_s(m_lst[i], n_lst)
    print(result)
