t = int(input())

x=[int(input()) for i in range(t)] #t동안 input된 값을 리스트에 추가
dp=[1]*(max(x)+1)

for i in range(2,4):
  for j in range(1,len(dp)):
    if j>=i:
      dp[j]+=dp[j-i]

for a in x:
  print(dp[a])