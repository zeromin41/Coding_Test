def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    # 원래 배열의 각 요소에 대해 내림차순 정렬된 배열에서의 인덱스 + 1을 순서로 부여
    answer = [sorted_emergency.index(e) + 1 for e in emergency]
    return answer