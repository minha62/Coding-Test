def cantour(num):
    # 선의 길이가 1일 때 
    if num == 1:
        return "-"
    else:
        # 문자열 3등분 했을때, 왼쪽과 오른쪽 문자열은 동일
        right_left_cantour = cantour(num//3)
        # 가운데 문자열 공백
        center = " " * (num//3)
        return right_left_cantour + center + right_left_cantour 

# 입력 개수를 모르므로 무한 반복으로 입력받고, EOF 에러 발생하면 프로그램 종료
while True:
    try:
        N = int(input())
        print(cantour(3**N))
    except:
        break
