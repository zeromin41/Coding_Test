class Solution {
    public int solution(int a, int b) {
        
        int concat = Integer.parseInt(a + "" + b);
        
        int sum = 2 * a * b;
        
        return Math.max(concat, sum);
    }
}