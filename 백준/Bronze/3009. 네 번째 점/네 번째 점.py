c=[]
d=[]
for i in range(3):
  a, b=map(int,input().split())
  c.append(a)
  d.append(b)
  c.sort()
  d.sort()
if c[0]==c[1]:
    print(c[2])
else:
    print(c[0], end=" ")
if d[0]==d[1]:
    print(d[2])
else:
    print(d[0])