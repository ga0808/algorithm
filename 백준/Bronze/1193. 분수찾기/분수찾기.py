n = int(input())
i=0
j=0

while j<n:
    i +=1
    j+=i

idx = j-n #4
if i%2!=0:
    print(str(idx+1)+"/"+str(i-idx))
elif i%2==0:
    print(str(i-idx)+"/"+str(idx+1))
