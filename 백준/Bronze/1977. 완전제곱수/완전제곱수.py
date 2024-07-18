m=int(input())
n=int(input())
list=[]

for i in range(m,n+1):
  if i ** (1/2) == int(i ** (1/2)):
    list.append(i)
if list:    
    print(sum(list))
    print(min(list))
else:
    print(-1)