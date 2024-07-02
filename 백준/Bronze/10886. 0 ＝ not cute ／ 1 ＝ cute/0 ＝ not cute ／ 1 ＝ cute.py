n = int(input())
l=[]
for i in range(n):
  m=int(input())
  l.append(m)
if l.count(1) > l.count(0):
  print('Junhee is cute!')
else:
  print('Junhee is not cute!')