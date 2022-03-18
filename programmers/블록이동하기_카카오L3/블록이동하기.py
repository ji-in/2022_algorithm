from collections import deque

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