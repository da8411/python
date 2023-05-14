T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    a=0;b=0;c=0;d=0;e=0
    while(num !=1):
        if (num % 11) == 0 :
            e+=1
            num = num / 11
        elif (num % 7) == 0:
            d+=1
            num = num / 7
        elif (num % 5) == 0:
            c+=1
            num = num / 5
        elif (num % 3) == 0:
            b+=1
            num = num / 3
        elif (num % 2) == 0:
            a+=1
            num = num / 2
    print(f"#{test_case} {a} {b} {c} {d} {e}")