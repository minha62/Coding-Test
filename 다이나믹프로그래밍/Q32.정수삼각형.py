n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(i+1):
        # 대각선 왼쪽
        if j == 0:
            left = 0
        else:
            left = array[i-1][j-1]
        # 대각선 오른쪽
        if j == i:
            right = 0
        else:
            right = array[i-1][j]
        array[i][j] = array[i][j] + max(left, right)

print(max(array[n-1]))
