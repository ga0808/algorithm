test_cnt = int(input())
for t in range(test_cnt):
    k = int(input()) #층
    n = int(input()) #호
    
    pre = [i for i in range(1,n+1)]

    for f in range(k):
        cur = [0]*n
        num = 0
        for p in range(n):
            num += pre[p]
            cur[p] = num
        pre = cur
    print(pre[n-1])