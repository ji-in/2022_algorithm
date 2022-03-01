from collections import defaultdict, deque

def bfs(graph, start, n):
    queue = deque()
    dist = [-1] * (n+1)
    queue.append(start)
    dist[start] = 0

    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if dist[node] == -1:
                dist[node] = dist[x] + 1
                queue.append(node)
    return dist

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for e in edge:
        a, b = e[0], e[1]
        if not b in graph[a]:
            graph[a].append(b)
        if not a in graph[b]:
            graph[b].append(a)
    for k in graph:
        graph[k].sort()

    dist = bfs(graph, 1, n)
    max_num = max(dist)
    for d in dist:
        if max_num == d:
            answer += 1
    return answer