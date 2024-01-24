def solution(numbers, hand):
    # l_x, l_y = 1, 4
    # r_x, r_y = 3, 4
    hand_pad = {"l":[1,4], "r":[3,4]}
    #키패드 2차원 좌표로 형상화
    key_pad = {"1":[1,1], "2":[2,1], "3":[3,1], "4":[1,2], "5":[2,2], "6":[3,2],
              "7":[1,3], "8":[2,3], "9":[3,3], "0":[2,4]}
    push_lst = [] #리스트로 추가안하고 그냥 answer=''이용해서 answer+='L'과 같이 문자 추가 가능
    #눌러야 할 버튼 케이스 나누기
    for n in numbers:
        # 무조건 오른손
        if n==3 or n ==6 or n==9:
            n = str(n)
            hand_pad["r"] = key_pad[n]
            push_lst.append("R")
            # r_y = key_pad[n][1]
        # 무조건 왼손
        elif n==1 or n==4 or n==7:
            n = str(n)
            hand_pad["l"] = key_pad[n]
            push_lst.append("L")
        # 2580
        elif n == 2 or  n == 5 or  n == 8 or  n == 0:
            n = str(n)
            #n과의 거리구하기 -> 계속 되는 연산은 위에 함수를 만들자
            l_n = abs(hand_pad["l"][0]-key_pad[n][0]) + abs(hand_pad["l"][1]-key_pad[n][1])
            r_n = abs(hand_pad["r"][0]-key_pad[n][0]) + abs(hand_pad["r"][1]-key_pad[n][1])

            #거리가 같으면, 주로 쓰는 손
            if l_n == r_n: #hand 첫글자 손을 n의 좌표로 업데이트
                hand_pad[hand[0]] = key_pad[n]
                push_lst.append(hand[0].upper())
            #거리 다르면 거리 비교
            elif (l_n > r_n):
                hand_pad["r"] = key_pad[n]
                push_lst.append("R")
            elif (l_n < r_n):
                hand_pad["l"] = key_pad[n]
                push_lst.append("L")
            else:
                pass
        else:
            pass
    answer = ''.join(push_lst)
    return answer