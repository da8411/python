T = int(input())

for test_case in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse =True)
    sum=0

    for j in range(0,K):
        sum += arr[j]
    sum = int(sum)

    print("#{} {}".format(test_case, sum))