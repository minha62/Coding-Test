[Problem link](https://www.softeer.ai/practice/6289)

```python
n, m = map(int, input().split())
w = list(map(int, input().split()))
result = 0

# 회원 간 친분관계
relation = [set() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    relation[a-1].add(b-1)
    relation[b-1].add(a-1)

for i in range(n):
    # 누구와도 친분이 없는 멤버는(empty relation) 본인이 최고라고 생각
    if not relation[i]:
        result += 1
        continue

    # i번째 회원이 자신이 최고라고 생각한다고 초기화
    best = True
    for j in relation[i]:
        # 친분이 있는 회원들 중 본인보다 무게가 높거나 같은 회원이 있다면 자신이 최고라고 생각하지X
        if w[i] <= w[j]:
            best = False
            break
    if best:
        result += 1

print(result)
```
