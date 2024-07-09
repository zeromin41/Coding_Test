t = int(input())
for i in range(t):
    n=int(input())
    l=[]
    k=[]
    for i in range(n):
      a,b=input().split()
      l.append(int(b))
      k.append(a)
    idx=l.index(max(l))
    print(k[idx]) 