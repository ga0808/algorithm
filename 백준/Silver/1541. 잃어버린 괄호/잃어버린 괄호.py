form = str(input())
res = 0
nums_lst=[]
num_lst = form.split("-")
for n in num_lst:
    num = n.split("+")
    nums_lst.append([int(i) for i in num])

sum_lst = [sum(ns) for ns in nums_lst]
for s in range(len(sum_lst)):
    if s==0:
        res += sum_lst[s]
    else:
        res -= sum_lst[s]
print(res)