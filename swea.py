T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    NM = input()
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if len(a_list) > len(b_list) :
        a_list, b_list = b_list, a_list

    li = []
    for k in range(len(b_list)-len(a_list)+1):
        sum = 0
        for j in range(len(a_list)):
            sum += a_list[j]*b_list[j+k]
        li.append(sum)
    print("#{} {}".format(test_case, max(li)))