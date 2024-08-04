t = int(input())
for i in range(t):
  total=0
  s=int(input())
  n=int(input())
  if n != 0 :
    for i in range(n):
      q, p=map(int,input().split())
      total+=q*p
  print(s+total)