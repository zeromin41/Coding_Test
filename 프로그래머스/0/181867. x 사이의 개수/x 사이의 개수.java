class Solution {
    public int[] solution(String myString) {
        String[] p = myString.split("x",-1);
        int[] answer = new int[p.length];

        for (int i = 0; i < p.length; i++) {
            answer[i] = p[i].length();
        }

        return answer;
    }
}