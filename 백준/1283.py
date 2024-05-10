N = int(input())
short_keys = [] # 단축키 저장
# in은 순차적으로 탐색해서 cost 높을 것. 이것보단 26개 bool 미리 만들어놓고 하는 게 더 효율적

for _ in range(N):
    words = list(input().split())
    is_first = False
    
    for i in range(len(words)):
        # 단어 첫 글자가 단축키로 지정되어 있지 않은 경우, 그 알파벳을 단축키로
        if words[i][0].upper() not in short_keys:
            is_first = True
            short_keys.append(words[i][0].upper())
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            print(' '.join(words))
            break
    
    # 단어 첫 글자가 이미 단축키로 지정되어 있는 경우
    if not is_first:
        for i in range(len(words)):
            flag = False
            for j in range(len(words[i])):
                if words[i][j].upper() not in short_keys:
                    flag = True
                    short_keys.append(words[i][j].upper())
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:] 
                    print(' '.join(words))
                    break
            if flag: break
            
        # 단축키로 지정할 수 없다면 그대로
        if not flag: print(' '.join(words))
