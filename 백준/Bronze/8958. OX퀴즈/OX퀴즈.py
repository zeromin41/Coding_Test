t = int(input())
for i in range(t):
    ox_list=list(input())
    score=0
    sum=0
    for j in ox_list:
        if j == 'O':
            score+=1
            sum+=score
        else:
            score=0
    print(sum)