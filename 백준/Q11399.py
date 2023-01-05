n = int(input())
array = list(map(int, input().split()))
array.sort()
result = 0

for i in range(n):
    result += (n-i) * array[i]
    
print(result)
