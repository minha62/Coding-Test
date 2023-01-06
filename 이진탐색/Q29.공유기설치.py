n, c = map(int, input().split())
houses = []
result = 0

for _ in range(n):
    houses.append(int(input()))
houses.sort()

start = 1 # 가능한 최소 거리
end = houses[-1] - houses[0] # 가능한 최대 거리

while start<=end:
    mid = (start+end)//2
    value = houses[0]
    cnt = 1
    
    for i in range(1,n):
        if houses[i] >= value+mid:
            value = houses[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        result = mid # 최적의 결과 저장
    else:
        end = mid - 1

print(result)
