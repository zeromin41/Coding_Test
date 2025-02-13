import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> solution(int[] num_list, int n) {
        List<Integer> result = new ArrayList<>();
        
        // n 번째부터 마지막까지
        for (int i = n - 1; i < num_list.length; i++) { 
            result.add(num_list[i]);
        }
        
        return result;
    }
}
