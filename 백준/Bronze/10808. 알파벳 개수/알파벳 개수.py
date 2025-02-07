s = input()
a = [0] * 26
for char in s:
    a[ord(char)-ord('a')] += 1
print(' '.join(map(str, a)))    # 리스트의 요소들을 문자열로 변환하고 공백으로 연결