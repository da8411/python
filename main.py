# baekjoon_2231

# 분해합 숫자 입력받고
# 분해합의 생성자를 찾아야함
# 이때, 분해합 = 찾아야 하는 생성자 + 각 자리 수 
# 생성자가 있다면, 가장 작은 생성자 출력
# 생성자가 없다면, 0 출력

n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)

# baekjoon_1018

# board 리스트에 전체 보드를 append() 함수를 통해 입력받기
# n-7과 m-7 범위의 중첩 for문을 작성 
# (문제 규칙상 칠할 체스는 8x8 크기로 정해져 있으므로)
# 7을 빼는 이유는 이 지점부터 8x8 크기의 체스판을 검사하기 때문에 전체 보드판 인덱스 벗어나면 안돼
#  i, j는 체스판의 칠할 부분을 찾는 시작점
# 시작점이 바뀔 때마다 처음부터 칠해주기 위해 draw 변수를 선언
# 시작 지점이 검은색일 경우와 흰색일 경우를 대비하여 2개의 변수를 준비
# 시작점인 i, j 지점부터 i+8, j+8 범위의 중첩 for문
# board[a][b] 지점이 2로 나눈 나머지가 0일 때와 1일 때 -> 언제 어느 색을 칠할지 결정
# if a + b 를 2로 나눈 나머지가 0: draw1은 검은색이 아닐때 1을 더하여 색칠
# draw2는 흰색이 아닐 때 1을 더하여 색칠 
# => 시작점이 검은색/흰색일 때 모두 해결
# min() 함수를 이용하여 가장 적은 횟수를 출력

n, m = map(int, input().split())
board = []
result = []
 
for _ in range(n):
    board.append(input())
 
for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0
 
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
 
        result.append(draw1)
        result.append(draw2)
 
print(min(result))

#baekjoon_1436

# n번째 수에 '666'이 포함되어 있다면(str이 아니면 무조건 1의자리부터 시작하니까)
# 카운트 +1
# if 카운트 수  = n 번째 수 => nth 출력 & while 종료

n = int(input())
nth = 666
count = 0

while True:
    if '666' in str(nth):
        count+=1
    if count == n: 
        print(nth)
        break
    nth+=1 