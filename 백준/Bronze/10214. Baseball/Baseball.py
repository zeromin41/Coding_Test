t=int(input())
for i in range(t):
  x=[]
  y=[]
  a=0
  b=0
  for i in range(9):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
  if sum(x)>sum(y):
    print("Yonsei")
  elif sum(x)<sum(y):
    print("Korea")
  else:
    print("Draw")
  