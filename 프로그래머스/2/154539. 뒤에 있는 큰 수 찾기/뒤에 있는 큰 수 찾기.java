import java.util.*;


class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Stack<Integer> stk = new Stack<>();
    
        Arrays.fill(answer, -1);
        
        for (int i = 0; i < numbers.length; i++) {
            while (!stk.isEmpty() && numbers[stk.peek()] < numbers[i]) {
                answer[stk.pop()] = numbers[i];
            }
            stk.push(i);
        }
        return answer;
    }
}