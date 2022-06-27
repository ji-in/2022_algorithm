def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        move -= 1
        # column
        q = [x[move] for x in board]
        idx = -1
        for i in range(len(q)):
            if q[i] != 0:
                bucket.append(q[i])
                idx = i
                board[i][move] = 0
                break

    stack = []
    while bucket:
        x = bucket.pop(0)
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
                answer += 2
            else:
                stack.append(x)
        
    return answer