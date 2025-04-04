from collections import deque

n,m=map(int,input().split())
grid=[list(map(int,input())) for _ in range(n)]
distance=[[0] * m for _ in range(n)]


dr =[-1,1,0,0]
dc =[0,0,-1,1]

start_r, start_c = 0,0 #시작위치 
if grid[start_r][start_c]==1:
    deq=deque([(start_r,start_c)]) # 큐에 시작점 넣고 초기화 
    distance[start_r][start_c] = 1
    
    # 이제 큐 초기화됐으니 이 안에서 진행
    while deq:
        current_r,current_c=deq.popleft()
        #다음 위치 구해야지 
        for i in range(4):
            next_r = current_r+dr[i]
            next_c = current_c+dc[i]
            # 조건 줘야지 1.맵안에있고 
            if 0<=next_r<n and 0<=next_c<m:
                #2. 1이면서 미방문일때때
                if grid[next_r][next_c]==1 and distance[next_r][next_c]==0:
                    # 다음 탐색을 위해 큐에 추가 
                    deq.append((next_r,next_c))
                    distance[next_r][next_c]=distance[current_r][current_c]+1
                    
print(distance[n-1][m-1])