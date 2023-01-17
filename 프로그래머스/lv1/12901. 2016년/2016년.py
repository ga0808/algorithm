def solution(a, b):
    answer = ''
    days = -1 #1월1일
    d_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    DOW = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    for i in range(1,a):
        days += d_dict[i]
    days += b
    return DOW[days%7]