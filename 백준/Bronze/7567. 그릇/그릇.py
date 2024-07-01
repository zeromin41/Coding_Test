dish = input()
firstdish=10

for i in range(1, len(dish)):
  if dish[i-1]==dish[i]:
    firstdish+=5
  else:
    firstdish+=10
print(firstdish)