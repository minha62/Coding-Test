from itertools import combinations

N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
result = 0

for num in range(2, N+1):
    # 두 문제 이상의 조합
    combi = list(combinations(problems, num))
    for c in combi:
        if (L <= sum(c) <= R) and (max(c) - min(c) >= X):
            result += 1

print(result)
