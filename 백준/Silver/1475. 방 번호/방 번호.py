def solve():
    """
    다솜이의 방 번호에 필요한 플라스틱 숫자 세트의 최소 개수를 계산합니다.

    Args:
        room_number: 다솜이의 방 번호 (문자열).

    Returns:
        필요한 플라스틱 숫자 세트의 최소 개수 (정수).
    """

    # 방 번호 입력 받기
    room_number = input()

    # 각 숫자의 빈도를 저장할 배열 초기화
    counts = [0] * 10

    # 방 번호의 각 숫자에 대해 빈도 증가
    for digit in room_number:
        counts[int(digit)] += 1

    # 6과 9의 빈도 합을 2로 나눈 후 올림하여 필요한 세트 수 계산
    six_nine_count = (counts[6] + counts[9] + 1) // 2
    counts[6] = six_nine_count
    counts[9] = six_nine_count

    # 가장 많이 사용된 숫자의 빈도를 찾아 필요한 세트 수 결정
    return max(counts)

print(solve())