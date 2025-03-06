n=int(input())
numbers=list(map(int,input().split()))
v=int(input())
cnt=0
for i in numbers:
    if i == v:
        cnt+=1
print(cnt)