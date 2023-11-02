[Problem Link](https://www.softeer.ai/practice/6294)

```python
n, k = map(int, input().split())
score = list(map(int, input().split()))

for _ in range(k):
  a, b = map(int, input().split())
  num = b - a + 1
  score_sum = sum(score[a-1:b])
  print(f"{(score_sum / num):.2f}")
```

> f"{변수/값:.2f}" → 소수점 2자리

> f"{변수/값:012d}" → 선행 0으로 채운 12자리 정수
