def solution(board, moves):
    answer = 0
    stack = []
        
    for mov in moves:
        for i in range(len(board)):
            if board[i][mov-1] == 0:
                continue
            
            last = board[i][mov-1]
            board[i][mov-1] = 0
            
            if stack and stack[-1] == last:
                stack.pop()
                answer += 2
            else:
                stack.append(last)
            break
            
    return answer
