n = int(input())
words = []
result = 0

for i in range(n):
    word = list(input())
    words.append(word)
    
for word in words:
    alp = []
    alp.append(word[0])
    check = 1
    
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            continue
        
        if word[i] in alp:
            check = 0
            break
        else:
            alp.append(word[i])
        
    if check == 1:
        result += 1
    
print(result)
