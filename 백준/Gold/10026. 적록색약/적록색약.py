from collections import deque

def bfs(r, c, color, current_visited, current_grid, n):
    q = deque([(r, c)])
    current_visited[r][c] = True
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not current_visited[nr][nc] and current_grid[nr][nc] == color:
                current_visited[nr][nc] = True
                q.append((nr, nc))


n = int(input())
grid = [input() for _ in range(n)] # 문자열 리스트로 받는게 더 편할 수 있음

# 1. 정상인 경우 계산
visited_normal = [[False] * n for _ in range(n)]
cnt_normal = 0
for r in range(n):
    for c in range(n):
        if not visited_normal[r][c]:
            cnt_normal += 1  # BFS 시작 전에 카운트!
            bfs(r, c, grid[r][c], visited_normal, grid, n)

# 2. 적록색약인 경우 계산 (R과 G를 같은 것으로 취급)
visited_rg = [[False] * n for _ in range(n)]
cnt_rg = 0

# 적록색약용 grid

def bfs_rg(r, c, current_visited, current_grid, n):
    q = deque([(r, c)])
    current_visited[r][c] = True
    original_color = current_grid[r][c]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not current_visited[nr][nc]:
                neighbor_color = current_grid[nr][nc]
                # 색 비교 로직 (핵심!)
                is_same_area = False
                if original_color in ('R', 'G'):
                    if neighbor_color in ('R', 'G'):
                        is_same_area = True
                elif original_color == 'B':
                    if neighbor_color == 'B':
                        is_same_area = True

                if is_same_area:
                    current_visited[nr][nc] = True
                    q.append((nr, nc))


for r in range(n):
    for c in range(n):
        if not visited_rg[r][c]:
            cnt_rg += 1 # BFS 시작 전에 카운트!
            bfs_rg(r, c, visited_rg, grid, n)

print(cnt_normal, cnt_rg)