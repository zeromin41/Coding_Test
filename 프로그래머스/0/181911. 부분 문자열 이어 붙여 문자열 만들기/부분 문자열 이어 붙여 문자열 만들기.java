class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        StringBuffer answer = new StringBuffer();
        
        for(int i = 0; i <my_strings.length; i++){
            int start = parts[i][0];
            int end = parts[i][1];
            
            answer.append(my_strings[i].substring(start, end + 1));
        }
        return answer.toString();
    }
}