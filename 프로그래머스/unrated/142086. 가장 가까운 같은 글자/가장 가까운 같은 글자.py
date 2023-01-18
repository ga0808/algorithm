def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            cnt=0
            for j in range(len(s[:i-1]),-1,-1):
                cnt+=1
                if s[i] == s[j]:
                    answer.append(cnt)
                    break
    return answer