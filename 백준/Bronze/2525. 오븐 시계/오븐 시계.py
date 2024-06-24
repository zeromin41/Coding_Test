a, b = map(int, input().split())
t = int(input())

a += t//60
b += t%60

if b>=60:
    a +=1
    b -=60
if a>=24:
    a-=24
print(a,b)