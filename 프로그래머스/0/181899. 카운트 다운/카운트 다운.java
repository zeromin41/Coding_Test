class Solution {
    public int[] solution(int start_num, int end_num) {
        
        int sn = start_num, en = end_num;
        int[] answer = new int[sn - en + 1];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = sn--;
        }

        return answer;
    }
}