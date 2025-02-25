# from collections import deque

# def solution(n):
#     cnt = 0
#     number_list = [i for i in range(1, n + 1)]
#     my_deque = deque(number_list)
    
#     def deq():
#         sum=0
#         for i in number_list:
#             if sum==n:
#                 cnt+=1
#                 return
#             sum += i
    
#     my_deque.popleft()
#     deq()
             
#     return cnt

# from collections import deque

# def solution(n):
#     cnt = 0
#     number_list = [i for i in range(1, n + 1)]

#     for i in range(1, n + 1):
#         my_deque = deque(number_list[i - 1:])
#         sum_val = 0
#         while my_deque:
#             val = my_deque.popleft()
#             sum_val += val
#             if sum_val == n:
#                 cnt += 1
#                 break
#             elif sum_val > n:
#                 break
#     return cnt

def solution(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 1:
                cnt += 1
            if n // i != i and (n // i) % 2 == 1:
                cnt += 1
    return cnt