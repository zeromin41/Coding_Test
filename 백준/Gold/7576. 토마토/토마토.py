from collections import deque

m,n=map(int,input().split())
tomatoes=[list(map(int,input().split())) for _ in range(n)]

# 거리 -1 초기화 ( 아직 안익음 (방문x))
distance = [[-1]*m for _ in range(n)]
q = deque()

#상하좌우 
dr=[-1,1,0,0]
dc=[0,0,-1,1]

# 익은토마토 1 위치 찾아서 큐에넣고 distnace 0 초기화
for r in range(n):
    for c in range(m):
        if tomatoes[r][c] ==1:
            q.append((r,c))
            distance[r][c]=0

while q:
    r, c = q.popleft()
    for i in range(4):
        nr , nc = r+dr[i], c+dc[i] #다음위치
        # 창고 범위 체크
        if 0<=nr<n and 0<=nc<m:
            # 해당칸이 0이고 방문하지않앗는지
            if tomatoes[nr][nc] == 0 and distance[nr][nc] == -1 :
                distance[nr][nc] = distance[r][c] +1
                q.append((nr,nc))
max_days =0
all_ripened = True
for r in range(n):
    for c in range(m):
        # 원래 익지 않았던 토마토(0) 칸을 확인
        if tomatoes[r][c] == 0:
            # 만약 BFS가 끝났는데도 distance가 -1이라면 -> 도달 불가, 안 익음
            if distance[r][c] == -1:
                all_ripened = False # 안 익은 토마토 발견
                break # 더 이상 확인할 필요 없이 루프 중단
            # 익었다면, 현재까지의 최대 날짜와 비교해서 더 큰 값으로 업데이트
            max_days = max(max_days, distance[r][c])
    # 안 익은 토마토를 발견해서 내부 루프가 중단되었다면, 외부 루프도 중단
    if not all_ripened:
        break

if all_ripened: # 만약 모든 토마토가 익었다면
    print(max_days) # 계산된 최대 날짜(최소 일수) 출력
else: # 안 익은 토마토가 하나라도 있다면
    print(-1)       # -1 출력