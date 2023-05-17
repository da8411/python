T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(money)) :
        if num//money[i] != 0 :
            change[i] = num//money[i]
            num = num%money[i]

    print("#{}".format(test_case))
    print(*list)