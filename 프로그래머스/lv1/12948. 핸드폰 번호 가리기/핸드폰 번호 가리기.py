def solution(phone_num):
    cnt = len(phone_num[:-4])
    answer_end = '*'*cnt + phone_num[-4:]
    return answer_end
