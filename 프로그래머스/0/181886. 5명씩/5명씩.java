import java.util.ArrayList;
class Solution {
    public String[] solution(String[] names) {
        ArrayList<String> list = new ArrayList<>();
        for(int i = 0; i < names.length; i += 5){
            list.add(names[i]);
        }
         String[] answer = new String[list.size()];
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}