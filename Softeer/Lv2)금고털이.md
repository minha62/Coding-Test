[Problem link](https://www.softeer.ai/practice/6288)

```python
w, n = map(int, input().split())
result = 0

jew = [list(map(int, input().split())) for _ in range(n)]

# 가격(p)가 높은순으로 정렬
jew.sort(key = lambda x : x[1], reverse=True)

for m, p in jew:
  # 배낭이 꽉 찼으면 종료
  if w == 0: break
  # 배낭 무게보다 i번째 귀금속의 무게가 작으면, 배낭에 담음
  if m <= w:
    result += (p * m)
    w -= m
  # 배낭 무게보다 i번째 귀금속 무게가 크면서 아직 배낭을 채울 수 있을 때, 남은 무게만큼 귀금속을 잘라 담음
  else:
    result += (w * p)
    w = 0

print(result)
```
