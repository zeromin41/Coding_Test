class Solution {
    public int solution(String[] order) {
        int sum = 0;
        
        for(int i = 0; i < order.length; i++){
            String s = order[i];
            
            if(s.contains("americano") || s.equals("anything")){
                sum += 4500;
            } else if(s.contains("cafelatte")){
                sum += 5000;
            }
        }
        return sum;
    }
}