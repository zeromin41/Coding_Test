def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    answer = 0

    for bab in babbling:
        for p in possible:
            if p * 2 not in bab: #같은 발음이 연속으로 사용되는 경우는 제외
                bab = bab.replace(p, ' ')
        if len(bab.strip()) == 0:
            answer += 1

    return answer