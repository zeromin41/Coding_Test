x = list(map(int,input().split()))

if (x[2] >= x[0] >= x[1]) or (x[1] >= x[0] >= x[2]):
  print(x[0])
elif (x[0] >= x[1] >= x[2]) or (x[2] >= x[1] >= x[0]):
  print(x[1])
elif (x[1] >= x[2] >= x[0]) or (x[0] >= x[2] >= x[1]):
  print(x[2])