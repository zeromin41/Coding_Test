import sys
input = sys.stdin.readline

n = int(input())
score = [0] * 2880	# 초 단위 정보가 담긴 배열
cnt = [0] * 2		# 각 팀 별 점수 계산을 위한 배열
ans = [0] * 2		# 각 팀 별 이긴 시간을 위한 배열

for _ in range(n):
    team, time = input().rstrip().split()
    score[int(time[:2]) * 60 + int(time[3:])] = team	# 입력 받은 시간을 초로 계산하여 배열에 팀 번호 저장

for i in range(2880):		# 초 단위로 모든 시간 탐색
    if score[i] == '1':		# 현재 시간에 1번 팀이 득점하는 경우
        cnt[0] += 1			# 1번 팀의 점수 증가
    elif score[i] == '2':	# 2번도 같음
        cnt[1] += 1
    
    if cnt[0] > cnt[1]:		# 현재 시간에 1번 팀의 점수가 더 높은 경우
        ans[0] += 1			# 1번 팀의 이긴 시간 증가
    elif cnt[1] > cnt[0]:	# 2번도 같음
        ans[1] += 1

for i in ans:				# 포맷에 맞추어 출력
    print(f"{i // 60:02}:{i % 60:02}")