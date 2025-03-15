l=[]
n=int(input())
for i in range(n):
    k=int(input())
    if (k==0):
        l.pop()
    else:
        l.append(k)
print(sum(l))
    