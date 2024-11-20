from collections import deque

def solution(numbers, target):
    queue = deque([(0,0)]) #현재합, 인덱스 0 으로 초기화
    count = 0
    
    while queue:
        (sum, idx) = queue.popleft() # 시작시(0,0)꺼내고 현재큐 비어있음
        if idx == len(numbers):
            if sum == target:
                count+=1
        else:
            queue.append((sum+numbers[idx],idx+1))
            queue.append((sum-numbers[idx],idx+1))
            
    return count