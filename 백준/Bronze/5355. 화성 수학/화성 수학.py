T = int(input())

for i in range(T):
  A = list(map(str, input().split()))
  B = float(A[0])
  for i in range(1, len(A)):
    if A[i] == '@':
      B *= 3
    elif A[i] == '%':
      B += 5
    elif A[i] == '#':
      B -= 7
  print('{:.2f}'.format(B))