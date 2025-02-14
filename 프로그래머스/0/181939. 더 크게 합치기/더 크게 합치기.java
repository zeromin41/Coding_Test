class Solution {
    public int solution(int a, int b) {
        
        int concatA = Integer.parseInt(a + "" + b);
        int concatB = Integer.parseInt(b + "" + a);
        
        return Math.max(concatA, concatB);
    }
}