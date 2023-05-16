T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    if (num[4] <= num[2]):
        b_num = num[1]
    elif num[4] > num[2]:
        a = num[4] - num[2]
        b_num = num[1] + num[3]*(a)

    a_num = num[0]*num[4]
    if (a_num <= b_num):
        total = a_num
    elif (a_num > b_num):
        total = b_num
        
    print("#{} {}".format(test_case, total))