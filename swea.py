for test_case in range(1, 11):
    N, N_list= input().split()
    N = int(N)
    new_list = []

    for i in N_list:
        if new_list and i == new_list[-1]:
            new_list.pop()
        else:
            new_list.append(i)
    print("#{} {}".format(test_case, ''.join(new_list)))