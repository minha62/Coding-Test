[Problem Link](https://www.softeer.ai/practice/6273)

```python
# 순열: permutations(객체, r)
# 조합: combinations(객체, r)
from itertools import permutations

N, M, K = map(int, input().split())
rails = list(map(int, input().split()))

perm_rails = permutations(rails, N)
result = 987654321

for rail in perm_rails: 
    weights = 0
    basket = 0
    num = 0
    i = 0

    while num < K:
        basket += rail[i]
        if basket > M:
            basket -= rail[i]
            weights += basket
            basket = 0
            num += 1
            continue
        i = (i + 1) % N
    result = min(result, weights)
print(result)
```
