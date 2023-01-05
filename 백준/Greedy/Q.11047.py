from bisect import bisect_right

n, k = map(int, input().split())
coins = []
result = 0

for _ in range(n):
    coins.append(int(input()))
    
not_use_idx = bisect_right(coins, k)

for x in range(not_use_idx-1, -1, -1):
    result += k // coins[x]
    k %= coins[x]
    if k == 0:
        break

print(result)
