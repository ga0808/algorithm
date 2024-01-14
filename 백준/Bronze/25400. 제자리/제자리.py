#첫번째로 입력되는 값 = 리스트의 길이
lst_len = int( input() )
#두번째로 입력되는 값 = 리스트
lst = list(map(int, input().split()))

#문제 분석
#카드 cnt개를 제거해서 - n번째에 숫자 n 카드가 위치할 경우를 만들어야함

#모든 카드가 제거할 경우 처리 필요 - 제자리 상태 아님
if 1 not in lst:
  print( len(lst) )
else:
  #몇개의 카드를 제거했는지 반환해야함
  cnt = 0
  find_n =1

  #1전의 카드 개수 + 1~2사이 카드 개수 + ...+  n-1~n 사이 카드 개수 의 합
  for l in lst:
    # print(l)
    if l != find_n: #다음으로 추가되는 수가 아니면
      cnt += 1 
      # print("cnt: ",cnt)
    else:
      find_n += 1
      # print(find_n)

  print(cnt)