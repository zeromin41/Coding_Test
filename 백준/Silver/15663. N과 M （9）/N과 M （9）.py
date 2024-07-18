n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()  # 수열을 오름차순으로 정렬
s = []
used = [False] * n  # 각 숫자의 사용 여부를 추적

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    prev = 0  # 같은 레벨에서 중복 출력을 방지하기 위한 변수
    for i in range(n):
        if not used[i] and x[i] != prev:  # 아직 사용하지 않은 숫자이고, 이전 숫자와 다른 경우
            s.append(x[i])
            used[i] = True
            dfs()
            s.pop()
            used[i] = False
            prev = x[i]

dfs()