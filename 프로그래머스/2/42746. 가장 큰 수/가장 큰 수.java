import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        List<Integer> list = new ArrayList<>();

        for (int number : numbers) {
            list.add(number);
        }

        // Sort by descending.
        Collections.sort(list, (o1, o2) -> {
            String s1 = String.valueOf(o1).repeat(4);
            String s2 = String.valueOf(o2).repeat(4);
            return s2.compareTo(s1);
        });

        StringBuilder sb = new StringBuilder();
        for (Integer item : list) {
            sb.append(item);
        }
        answer = sb.toString();

        if (answer.charAt(0) == '0') {
            return "0";
        }
        return answer;
    }
}