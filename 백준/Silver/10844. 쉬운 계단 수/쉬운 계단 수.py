n = int(input())
if n == 1:
    print(9)

else:
    pre = [0]+[1]*9
    for j in range(n-1):
        cur = [pre[1]] + [0]*8 + [pre[-2]]
        for i in range(1,9):
            cur[i] = pre[i-1] + pre[i+1]

        pre = cur
    print(sum(pre)%1000000000)