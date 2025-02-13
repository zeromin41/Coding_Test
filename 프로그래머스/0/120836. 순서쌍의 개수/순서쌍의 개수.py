def solution(n):
    answer = len([(i,n//i) for i in range(1,n+1) if n%i ==0])
    return answer 
    #리스트 컴프리헨션 [표현식 for 변수 in 반복가능한객체 if 조건문]
