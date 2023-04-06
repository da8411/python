def do_yo_wanna_build_a_snowman(N, snowballs):
    height_diff = 9999999999
    
    for i in range(N):
        for j in range(i + 3, N):
            snowman1 = snowballs[i] + snowballs[j]
            left, right = i + 1, j - 1

            while left < right:
                snowman2 = snowballs[left] + snowballs[right]
                if abs(snowman2 - snowman1) < height_diff:
                    height_diff = abs(snowman2 - snowman1)

                if snowman2 < snowman1:
                    left += 1
                elif snowman2 > snowman1:
                    right -= 1
                else:
                    return 0

    return height_diff


if __name__ == "__main__":
    N = int(input())
    snowballs = sorted(list(map(int,input().split())))
    print(do_yo_wanna_build_a_snowman(N, snowballs))