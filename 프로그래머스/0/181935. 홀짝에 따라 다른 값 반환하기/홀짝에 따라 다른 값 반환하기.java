class Solution {
    public int solution(int n) {
        // 재귀 종료
        if (n <= 0) {
            return 0;
        }
        
        int answer = 0;
        
        if (n % 2 == 1) { 
            answer = n + solution(n - 2);
        } else { 
            answer = (n * n) + solution(n - 2);
        }
        
        return answer;
    }
}
