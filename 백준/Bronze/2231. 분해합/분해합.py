num = input()

num_len = len(num)
ans = []

def dfs(first_chk, tmp):

    if num_len == len(tmp):
        tmp_sum = int(tmp)
        for t in tmp:
            tmp_sum += int(t)
        if tmp_sum == int(num):
            ans.append(int(tmp))
        return 0

    if first_chk: 
        first_chk = False
        for i in range(10):
            tmp += str(i)
            dfs(first_chk, tmp)
            tmp = tmp[:-1]
            first_chk = True

    else :
        for i in range(10):
            tmp += str(i)
            dfs(first_chk, tmp)
            tmp = tmp[:-1]

    
for n in range(0,int(num[0])+1):
    dfs(True, str(n))

if len(ans)==0:
    print(0)
else:
    print(min(ans))