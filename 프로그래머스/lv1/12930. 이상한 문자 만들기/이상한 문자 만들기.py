def solution(s): #짝수 대문자, 홀수 소문자
    answer = ''
    s_lst = s.split(" ")
    for j in range(0,len(s_lst)):
        word = s_lst[j]
        for i in range(0,len(word)):
            if i%2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
#         if word != s_lst[-1]:
#             answer += ' '
        answer+= ' '
    return answer[0:-1]