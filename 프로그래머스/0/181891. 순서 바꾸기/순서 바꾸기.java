class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] result = new int[num_list.length];
        
        int index = 0;  //n이후 배열 앞으로
        for (int i = n; i < num_list.length; i++) {
            result[index] = num_list[i];
            index++;
        }
        
        for (int i = 0; i < n; i++) {   //n이전 배열 뒤로
            result[index] = num_list[i];
            index++;
        }
        
        return result;
    }
}