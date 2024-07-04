while True:
    n = int(input())
    if n == -1:
        break
    
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    
    total = 0
    for num in l:
        total += num
    
    if n == total:
        print(f"{n} = {' + '.join(map(str, l))}")
    else:
        print(f"{n} is NOT perfect.")
