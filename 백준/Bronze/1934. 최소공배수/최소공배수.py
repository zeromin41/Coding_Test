import math
t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    print(math.lcm(a,b))    

#파이썬은 math 모듈에 최소공배수 구하는 lcm함수와 최대공약수 구하는 gcd 함수가 있다!!
#t = int(input())

'''
for i in range(t):
    a,b = map(int,input().split())
    r = a*b
    while b>0:
      a,b = b,a%b

    print(r//a)
'''