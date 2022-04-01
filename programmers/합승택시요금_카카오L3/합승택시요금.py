import heapq

def solution(n, s, a, b, fares):

    INF = int(1e9)
    graph = [[] for _ in range(n+1)]

    for fare in fares:
        x, y, z = fare
        graph[x].append((y, z))
        graph[y].append((x, z))

    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    answer = INF
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer