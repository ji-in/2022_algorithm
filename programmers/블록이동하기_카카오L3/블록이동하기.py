from collections import deque

<<<<<<< HEAD
def solution(board):
    answer = 0
    n = len(board)
    dist = [[-1]*n for _ in range(n)]
    queue = deque()
    dist[0][0], dist[0][1] = 0, 0
    queue.append([0, 0, 0, 1])
    DIR = 0

    while queue:
        x1, y1, x2, y2 = queue.popleft()
        if DIR == 0: # 가로
            # 오
            nx, ny = x2, y2+1
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x2][y2] + 1
                    queue.append([x2, y2, nx, ny])
            # 왼
            nx, ny = x1, y1-1
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x1][y1] + 1
                    queue.append([nx, ny, x1, y1])
            # 90도 회전
            # 축이 x1, y1
            # 상
            if 0<= x1-1 <n and 0<= y1+1 <n and board[x1-1][y1] == 0 and board[x1-1][y1+1] == 0:
                nx, ny = x1-1, y1
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x1][y1] + 1
                    queue.append([nx, ny, x1, y1])
                    DIR = 1
            # 하
            if 0<= x1+1 <n and 0<= y1+1 <n and board[x1+1][y1] == 0 and board[x1+1][y1+1] == 0:
                nx, ny = x1+1, y1
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x1][y1] + 1
                    queue.append([x1, y1, nx, ny])
                    DIR = 1
            # 축이 x2, y2
            # 상
            if 0<= x2-1 <n and 0<= y2-1 <n and board[x2-1][y2] == 0 and board[x2-1][y2-1] == 0:
                nx, ny = x2-1, y2
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x2][y2] + 1
                    queue.append([nx, ny, x2, y2])
                    DIR = 1
            # 하
            if 0<= x2+1 <n and 0<= y2-1 <n and board[x2+1][y2] == 0 and board[x2+1][y2-1] == 0:
                nx, ny = x2+1, y2
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x2][y2] + 1
                    queue.append([x2, y2, nx, ny])
                    DIR = 1
        else: # 세로
            # 상
            nx, ny = x1-1, y1
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x1][y1] + 1
                    queue.append([nx, ny, x1, y1])
            # 하
            nx, ny = x2+1, y2
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x2][y2] + 1
                    queue.append([x2, y2, nx, ny])
            # 90도 회전
            # 오
            if 0<= x1+1 <n and 0<= y1+1 <n and board[x1][y1+1] == 0 and board[x1+1][y1+1] == 0:
                nx, ny= x1, y1+1
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x1][y1] + 1
                    queue.append([x1, y1, nx, ny])
                    DIR = 0
            # 왼
            if 0<= x1+1 <n and 0<= y1-1 <n and board[x1][y1-1] == 0 and board[x1+1][y1-1] == 0:
                nx, ny= x1, y1-1
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x1][y1] + 1
                    queue.append([nx, ny, x1, y1])
                    DIR = 0
            # 축이 x2, y2
            # 오
            if 0<= x2-1 <n and 0<= y2+1 <n and board[x2][y2+1] == 0 and board[x2-1][y2+1] == 0:
                nx, ny= x2, y2+1
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x2][y2] + 1
                    queue.append([x2, y2, nx, ny])
                    DIR = 0
            # 왼
            if 0<= x2-1 <n and 0<= y2-1 <n and board[x2][y2-1] == 0 and board[x2-1][y2-1] == 0:
                nx, ny= x2, y2-1
                if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x2][y2] + 1
                    queue.append([nx, ny, x2, y2])
                    DIR = 0

        print('###################')
        for i in range(n):
            for j in range(n):
                print(dist[i][j], end=' ')
            print()
    return dist[n-1][n-1]

board = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
solution(board)
=======
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
>>>>>>> 3f14998f739078e7fd77feb32905f51bcc9e4f3a
