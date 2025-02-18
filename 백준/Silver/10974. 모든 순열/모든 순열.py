n = int(input())
l = []

def dfs():
    if len(l) == n:
        print(*l)
        return
    for i in range(1, n + 1):
        if i not in l:
            l.append(i)
            dfs()
            l.pop()

dfs()