class Solution {
    public int solution(int[] arr1, int[] arr2) {  
        // 배열 길이 비교
        if (arr1.length > arr2.length) return 1;
        if (arr1.length < arr2.length) return -1;
        // 배열 원소의 합 비교
        int sum1 = 0, sum2 = 0;
        for (int num : arr1) sum1 += num;
        for (int num : arr2) sum2 += num;
        // 합 비교 후 결과 반환
        return Integer.compare(sum1, sum2);
    }
}