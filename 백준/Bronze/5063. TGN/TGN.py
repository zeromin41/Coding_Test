n = int(input())
for i in range (n):
  r,e,c=map(int,input().split())
#광고를 하지않을때 수익, 광고를 했을때 수익, 광고비용
  if r>e-c:
    print("do not advertise")
  elif r==e-c:
    print("does not matter")
  else:
    print("advertise")