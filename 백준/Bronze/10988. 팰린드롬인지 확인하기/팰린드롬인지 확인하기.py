w=list(str(input()))
x=[]
for i in range(1,len(w)//2+1): 
     if w[i-1]==w[-i]:
      x.append(1)
     else:
      x.append(0)
if 0 in x: 
  print(0)
else: 
  print(1)


#파이썬 내장함수 reversed 사용하면 아주 쉬웠던 문제네욤..ㅎ
