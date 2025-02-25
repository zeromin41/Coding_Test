def solution(n):
    def count_ones(num):
        return bin(num).count('1')

    ones = count_ones(n)
    next_num = n + 1
    while True:
        if count_ones(next_num) == ones:
            return next_num
        next_num += 1