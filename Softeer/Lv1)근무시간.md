[Problem link](https://www.softeer.ai/practice/6254)
```python
result = 0
for _ in range(5):
  start, end = input().split()
  start_h, start_m = start.split(":")
  end_h, end_m = end.split(":")
  result += ((int(end_h) - int(start_h)) * 60 + (int(end_m) - int(start_m)))

print(result)
```
