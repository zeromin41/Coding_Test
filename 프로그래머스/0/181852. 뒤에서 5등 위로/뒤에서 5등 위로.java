import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        Arrays.sort(num_list);

        int[] answer = Arrays.copyOfRange(num_list, 5, num_list.length); // 5부터 끝까지 
        
        return answer;
    }
}
