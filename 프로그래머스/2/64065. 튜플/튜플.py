def solution(s):
    nums = set()
    s_lst = []
    num = ""
    s = s[1:-1]
    
    for idx, i in enumerate(s) :
        if i == "{":
            continue
        elif i == "," and s[idx-1]!="}":
            nums.add(int(num))
            num = ""
            continue
        elif i == "," :
            continue
        elif i == "}":
            nums.add(int(num))
            num=""
            s_lst.append(nums)
            nums = set()
            continue
        num+=i
        # print(num)
        
    answer = []
    s_lst = sorted(s_lst, key=len)
    for idx, s_ in enumerate(s_lst):
        if idx == 0:
            answer.append(list(s_)[0])
            continue    
        s_ = s_.difference(s_lst[idx-1])
        answer.append(list(s_)[0])
    return answer