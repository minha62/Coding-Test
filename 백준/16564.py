# 이분 탐색
N, K = map(int, input().split())
levels = [int(input()) for _ in range(N)]

levels.sort()
left, right = levels[0], levels[-1] + K

def get_needed_levels(mid):
    needed_levels = 0
    for level in levels:
        if level < mid:
            needed_levels = needed_levels + mid - level
        else: break
    return needed_levels

while left <= right: # 등호 없으면 틀리는 테스트케이스 있음
    mid = (left + right) // 2
    needed_levels = get_needed_levels(mid)
    if needed_levels <= K:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)
