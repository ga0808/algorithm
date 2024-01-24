#피보나치 - 하향식 동적 계획법 : 조건 : n>=1      #top-down

#메모이제이션할 리스트 생성
n = int(input())
dp = [-1]*n
#피보나치 1,2 => 1
dp[0:2] = [1,1]

def fibo_dp_tdown(n):
  #어차피 계산 안된 것만 계산 할텐데, 피보나치 1,2는 이미 계산이 되어서 음수에 대한 피보나치 값을 구하는 상황이 발생하지 않음 
  # if n ==1 or n==2:
  #   return 1

  #재귀로 하면 - 반복되는게 너무 많으니까, 메모이제이션 할 리스트에 이미 계산 되었는지 확인해야함
  if dp[n-1] == -1: #계산이 안되어 -1이라면
      dp[n-1] = fibo_dp_tdown(n - 1) + fibo_dp_tdown(n - 2)
  return dp[n-1]

print(fibo_dp_tdown(n))
