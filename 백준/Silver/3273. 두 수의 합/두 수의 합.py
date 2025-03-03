def count_pairs(n, sequence, x):
    sequence.sort() 
    left, right = 0, n - 1
    count = 0

    while left < right:
        current_sum = sequence[left] + sequence[right]
        if current_sum == x:
            count += 1
            left += 1
            right -= 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1

    return count
n = int(input())
sequence = list(map(int, input().split()))
x = int(input())
print(count_pairs(n, sequence, x))