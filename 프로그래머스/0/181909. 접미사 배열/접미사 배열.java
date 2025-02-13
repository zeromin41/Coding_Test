import java.util.Arrays;

class Solution {
    public String[] solution(String my_string) {
        int length = my_string.length();
        String[] answer = new String[length];

        //접미사 생성
        for (int i = 0; i < length; i++) {
            answer[i] = my_string.substring(i); // i번째부터 끝까지의 문자열 저장
        }

        //정렬
        Arrays.sort(answer);

        return answer;
    }
}