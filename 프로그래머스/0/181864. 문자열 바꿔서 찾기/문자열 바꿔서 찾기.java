class Solution {
    public int solution(String myString, String pat) {
        myString = myString.replace("A","X").replace("B","A").replace("X","B");
     
        int answer = myString.contains(pat)?1:0;
        return answer;
    }
}