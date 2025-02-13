class Solution {
    public String[] solution(String my_string) {
        String[] answer = my_string.trim().split("\\s+"); //trim이 양옆공백제거
        return answer;
    }
}