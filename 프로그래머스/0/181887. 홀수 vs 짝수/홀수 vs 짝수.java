class Solution {
    public int solution(int[] num_list) {
        int o_sum = 0;
        int e_sum = 0;
        for (int i = 0; i<num_list.length; i+=2){
            o_sum+=num_list[i];
        }
        for (int i = 1; i<num_list.length; i+=2){
            e_sum+=num_list[i];;
        }
        if (o_sum >= e_sum) {
            return o_sum;
        } else{
            return e_sum;
        }
    }
}