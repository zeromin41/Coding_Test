n = int(input())
for i in range (n):
  a,b = map(int,input().split())
  x = a // b
  y = a % b
  print(f"You get {x} piece(s) and your dad gets {y} piece(s).")