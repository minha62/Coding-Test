n = int(input())
dp = [[0, 0]] * (n+1)
result = [0, []]

for i in range(2, n+1):
    # 연산3: 1을 뺀다
    # 3번째 연산은 언제나 가능하므로 dp[i]를 연산3으로 초기화
    dp[i] = [dp[i - 1][0] + 1, i - 1]
    
    # 연산2: 2로 나눠떨어지면 2로 나눈다
    # 위에서 초기화한 dp[i]보다 값이 더 작을 때만 갱신
    if (i % 2 == 0 and dp[i // 2][0] < dp[i][0]):
        dp[i] = [dp[i // 2][0] + 1, i // 2]
        
    # 연산1: 3으로 나누어 떨어지면, 3으로 나눈다
    # 위에서 초기화한 dp[i]보다 값이 더 작을 때만 갱신
    if (i % 3 == 0 and dp[i // 3][0] < dp[i][0]):
        dp[i] = [dp[i // 3][0] + 1, i // 3]

result[0] = dp[n][0]

tmp = n
while tmp != 0:
    result[1].append(tmp)
    tmp = dp[tmp][1]
    
print(result[0])
print(*result[1])
