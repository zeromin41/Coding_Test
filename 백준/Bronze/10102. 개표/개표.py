a=int(input())
b=list(input())
if b.count('A')>b.count('B'):
  print('A')
elif b.count('B')>b.count('A'):
  print('B')
else:
  print('Tie')
