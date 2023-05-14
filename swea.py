# 평균값 구하기
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램 (소수점 첫째 자리에서 반올림한 정수 출력)
# 각 수는 0 이상 10000 이하의 정수
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력

T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    avg = sum(num) / len(num)
    avg_num = round(avg)
    print('#{} {}'.format(test_case, avg_num))


#2070
T = int(input())
for test_case in range(1, T + 1):
    a,b=map(int, input().split())
    if a>b:
        print(f"#{test_case} > ")
    elif a<b:
        print(f"#{test_case} < ")
    else:
        print(f"#{test_case} = ")