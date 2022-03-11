n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
max = nums[n - 1]
next_max = nums[n - 2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += max
    m -= 1
  
  if m == 0:
    break
    
  result += next_max
  m -= 1

print(result)
