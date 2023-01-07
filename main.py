#첫째줄에 테스트 케이스
#각 테스트케이스 마다 n, m 입력
#n과 m은 각각 행과 열을 의미
#행렬은 첫번째 행부터 1줄로 입력받음

#점화식 
#d[i][j] = matrix[i][j] + max(d[i-1][j], d[i-1][j-1], d[i-1][j+1]
import sys
T = int(input())

for k in range(T):
  n, m = map(int, sys.stdin.readline().split())

  #1차원 리스트로 입력받아서 matrix에 이차원 리스트로 만들어주기
  input_list = list(map(int, sys.stdin.readline().split()))

  count = 0
  matrix = []
  for i in range(n):
    tmp = []
    for j in range(m):
      tmp.append(input_list[count])
      count += 1
    matrix.append(tmp)

  
  dp = [[0] * m for _ in range(n)]

  #dp테이블 초기값 세팅
  for i in range(n):
    dp[i][0] = matrix[i][0]

  #dp테이블 작성
  for i in range(n):
    for j in range(1, m):
      if(i == 0):
        dp[i][j] = matrix[i][j] + max(dp[i][j-1], dp[i+1][j-1])

      elif(i== n-1):
        dp[i][j] = matrix[i][j] + max(dp[i][j-1], dp[i-1][j-1])
    
      else:
        dp[i][j] = matrix[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

  result = -1
  for i in range(0, n):
    if(dp[i][m-1] > result):
      result = dp[i][m-1]

  print(result)
        