from collections import deque

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    distance[start_x][start_y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 상하좌우 방향으로 이동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:  # 미로의 범위 안에 있어야 함
                if not visited[nx][ny] and maze[nx][ny] == '1':  # 방문하지 않았고 이동 가능한 칸인 경우
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                    
                    if nx == N - 1 and ny == M - 1:  # 도착점에 도달한 경우
                        return distance[nx][ny]
    
    # 도착점에 도달하지 못한 경우는 문제 조건에 의해 항상 도착할 수 있는 입력만 주어짐
    return -1

# 입력 처리
N, M = map(int, input().split())
maze = [input() for _ in range(N)]

# 방문 여부와 거리를 저장할 배열 초기화
visited = [[False] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]

# BFS 시작
min_distance = bfs(0, 0)

# 결과 출력
print(min_distance)
