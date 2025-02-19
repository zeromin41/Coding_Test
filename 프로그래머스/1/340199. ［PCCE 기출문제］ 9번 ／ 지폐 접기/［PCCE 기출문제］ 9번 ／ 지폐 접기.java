import java.util.Arrays;

class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        Arrays.sort(wallet); // 지갑 크기 오름차순으로 정렬
        Arrays.sort(bill);   // 지폐 크기를 오름차순으로 정렬

        while (bill[0] > wallet[0] || bill[1] > wallet[1]) {
            if (bill[0] > bill[1]) {
                bill[0] /= 2;
            } else {
                bill[1] /= 2;
            }
            Arrays.sort(bill); // 지폐 크기 다시 정렬
            answer++;
        }
        return answer;
    }
}