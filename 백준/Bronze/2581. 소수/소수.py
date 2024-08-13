m=int(input())
n=int(input())
s=[]

for i in range(max(2,m),n+1): # 60일때
    for j in range(2,i): # 2~59까지 60을 나누기
      if i%j==0:    # 나눠진다면 해당 for문 종료
        break
    else:    # 아니면 배열에 추가
      s.append(i)
if s==[]:
  print(-1)
else:
  print(sum(s))
  print(min(s))