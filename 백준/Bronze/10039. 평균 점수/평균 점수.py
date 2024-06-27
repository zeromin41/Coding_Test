total = 0 #for문 안에서 입력된 각 i값들을 모두 더한 총합을 생각하기!
for i in range(5):
  i = int(input())
  if i < 40:
    i = 40
  else:
    i = i
  total+=i #for문안에서 총합 구하기!
print(int(total/5))