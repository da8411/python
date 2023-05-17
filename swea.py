T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    time = 0
    if C < A:
        time = A - C
    elif C >= A | C <= B:
        time = 0
    elif C > B:
        time = -1

    print("#{} {}".format(test_case, time))