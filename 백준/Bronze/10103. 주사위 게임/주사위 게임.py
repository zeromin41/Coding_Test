n = int(input())
ascore=bscore=100
for i in range(n):
  a,b=map(int,input().split())
  if a<b:
    ascore-=b
  if a>b:
    bscore-=a
print(ascore)
print(bscore)