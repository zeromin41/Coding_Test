n = int(input())

result = 0
cnt = 0
while True:
  cnt += 1
  result += cnt
  if result > n:
    break
print(cnt-1)