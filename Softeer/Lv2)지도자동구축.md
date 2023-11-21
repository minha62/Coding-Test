[Problem Link](https://www.softeer.ai/practice/6280)

> DP 사용 안하는 경우
```python
N = int(input())
result = 0
dots_per_line = 2 # 한 변에 존재하는 점의 개수

for n in range(N):
    dots_per_line += pow(2, n)
# 전체 점 개수 = 한 변에 존재하는 점의 개수의 제곱
result = dots_per_line ** 2

print(result)
```

> DP 사용하는 경우
```python
N = int(input())

# 한 변에 존재하는 점 개수
dp = [0] * 16
dp[0] = 2

# dp[i] = dp[i-1] + 2^(i-1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + (2 ** (i-1))
# 전체 점 개수 = 한 변에 존재하는 점의 개수의 제곱
result = dp[N] ** 2
print(result)
```

실행시간과 메모리는 거의 동일
