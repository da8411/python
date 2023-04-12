if __name__ == '__main__':
    A = input()
    B = input()

    # dp[i][j] : A의 i번째까지의 문자열과 B의 j번째까지의 문자열의 LCS
    dp = [['' for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        nowA = A[i-1]
        for j in range(1, len(B) + 1):
            nowB = B[j-1]

            if nowA == nowB:  # 두 문자가 같을 경우
                dp[i][j] = dp[i-1][j-1] + nowA
            else:  # 두 문자가 다를 경우
                if len(dp[i][j-1]) > len(dp[i-1][j]):
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

    print(len(dp[len(A)][len(B)]))

    if len(dp[len(A)][len(B)]) != 0:
        print(dp[len(A)][len(B)])