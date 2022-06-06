from collections import deque

def can_move(cur1, cur2, new_board):
    x, y = 0, 1
    cand = []
    
    # 평행이동
    dic = {0: [-1, 0], 1: [1, 0], 2: [0, 1], 3: [0, -1]} # 위, 아래, 오, 왼
    for i in range(4):
        nx1 = (cur1[x] + dic[i][x], cur1[y] + dic[i][y])
        nx2 = (cur2[x] + dic[i][x], cur2[y] + dic[i][y])
        if new_board[nx1[x]][nx1[y]] == 0 and new_board[nx2[x]][nx2[y]] == 0:
            cand.append((nx1, nx2))
    
    # 회전
    if cur1[x] == cur2[x]: # 가로
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[x]+d][cur1[y]] == 0 and new_board[cur2[x]+d][cur2[y]] == 0:
                cand.append((cur1, (cur1[x]+d, cur1[y])))
                cand.append((cur2, (cur2[x]+d, cur2[y])))
                
    else: # 세로
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[x]][cur1[y]+d] == 0 and new_board[cur2[x]][cur2[y]+d] == 0:
                cand.append(((cur1[x], cur1[y]+d), cur1))
                cand.append(((cur2[x], cur2[y]+d), cur2))
    return cand

def solution(board):
    
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    
    # board 외벽 둘러싸기
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    q = deque([((1, 1), (1, 2), 0)]) # 첫 번째 좌표, 두 번째 좌표, 시간
    check = set([((1, 1), (1, 2))]) # 방문 확인
    
    while q:
        cur1, cur2, time = q.popleft()
        if cur1 == (n, n) or cur2 == (n, n):
            return time
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in check:
                q.append((nxt[0], nxt[1], time+1))
                check.add(nxt)
