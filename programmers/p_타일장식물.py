def solution(N):
    answer = 0
    dp = [1, 1]

    for i in range(N + 1):
        if i > 1:
            dp.append(dp[i - 1] + dp[i - 2])

    # print(dp)

    return dp[len(dp) - 1] * 2 + dp[len(dp) - 2] * 2

if __name__ == '__main__':
    N = 5
    # N = 6

    print(solution(N))