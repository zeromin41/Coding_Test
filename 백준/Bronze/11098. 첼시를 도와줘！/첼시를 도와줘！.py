n = int(input())

for i in range (n):
    max=0
    maxName=""
    t = int(input())
    for i in range (t):
        num, name = input().split()
        num=int(num)
        if num > max:
          max = num
          maxName = name
    print(maxName)
