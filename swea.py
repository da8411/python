T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    sum = 0

    for i in range(0,5):
        if arr[i] < 40:
            arr[i] = 40
        sum += arr[i]
    avg = sum / len(arr)
    avg = int(avg)

    print(f"#{test_case} {avg}")