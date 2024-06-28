x=list(map(int,input().split()))
len(x)==3
if x[0]==x[1]==x[2]:
  print(10000+x[0]*1000)
elif x[0]==x[1] or x[1]==x[2] or x[0]==x[2]:
  x.sort()
  print(1000+x[1]*100)
else:
  x.sort()
  print(x[2]*100) #x.max()로도 가능