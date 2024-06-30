n = int(input())
a=[]
for i in range(n):
  x = list(map(int, input().split()))
  if x[0]==x[1]==x[2]:
    q=10000+x[0]*1000
    a.append(q)
  elif x[0]==x[1] or x[1]==x[2]:
    w=1000+x[1]*100
    a.append(w)
  elif x[0]==x[2]:
    e=1000+x[0]*100
    a.append(e)
  else:
    r=max(x)*100
    a.append(r)
print(max(a))