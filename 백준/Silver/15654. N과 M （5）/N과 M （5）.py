n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        if x[i] in s:
            continue
        s.append(x[i])
        dfs()
        s.pop()

dfs()
