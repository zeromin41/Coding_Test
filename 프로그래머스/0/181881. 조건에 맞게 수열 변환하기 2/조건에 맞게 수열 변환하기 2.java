import java.util.Arrays;
class Solution {
    public int solution(int[] arr) {
        int count = 0;
        int[] copyArr; //선언만
        while(true){
             // 4. 새 값 다시 복사해서 넣음
             copyArr = Arrays.copyOf(arr, arr.length); // 1. 원본 복사값 할당
            // System.out.println("변경전복사 "+Arrays.toString(copyArr));
             // 2. 원본에 새 값 들어감
            for(int i = 0; i < arr.length; i++){
                if(arr[i] >= 50 && arr[i] % 2 == 0){
                    arr[i] /= 2;
                } else if(arr[i] < 50 && arr[i] % 2 == 1){
                    arr[i] = arr[i] *2 + 1;
                }
            }
            // System.out.println("원본 "+Arrays.toString(arr));
            // System.out.println("변경복사 "+Arrays.toString(copyArr));

            // 3. 비교해보고 같지 않다면 안나가고 count만 1 up
            if(Arrays.equals(copyArr, arr)) {
                break;
            }
            count++;
        }
        return count;

    }
}