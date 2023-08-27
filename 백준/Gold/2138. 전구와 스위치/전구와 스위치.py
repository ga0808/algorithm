n = int(input())
cur = [int(i) for i in input()]
res = [int(i) for i in input()]

#첫번째 스위치 누름
first_on = cur.copy()
first_on[0] = 1-first_on[0]
first_on[1] = 1-first_on[1]
on_tap = 1

for i in range(1,len(cur)): # 1,2
    if first_on[i-1] != res[i-1]:
        on_tap += 1

        if i != n-1:
            range_end = i+2
        else:
            range_end = i+1
            
        for j in range(i-1,range_end):
            first_on[j] = 1 - first_on[j]

#첫번째 스위치 안누름
off_tap = 0
for i in range(1,len(cur)): # 1,2
    if cur[i-1] != res[i-1]:
        off_tap += 1
        
        if i != n-1:
            range_end = i+2
        else:
            range_end = i+1
            
        for j in range(i-1,range_end):
            cur[j] = 1 - cur[j]

#확인
if first_on != res and cur != res:
    print(-1)
elif first_on == res and cur == res:
    print(min(on_tap , off_tap))
else:
    if first_on == res:
        print(on_tap)
    else:
        print(off_tap)