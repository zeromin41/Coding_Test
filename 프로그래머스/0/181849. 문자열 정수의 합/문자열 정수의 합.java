class Solution {
    public int solution(String num_str) {
        int numArray[] = new int[num_str.length()];
        int answer = 0;
        for (int i =0; i<num_str.length(); i++){
            numArray[i] = num_str.charAt(i)-'0';
            answer += numArray[i]; //합계 계산
        }
        return answer;
    }
}
    