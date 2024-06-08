import java.util.*;

class Solution {

    public int solution(String s) {
        int answer = 0;
        String curr = s;

        for (int i = 0; i < s.length(); i++) {
            curr = rotate(curr);
            
            if (isValidParentheses(curr)) {
                answer++;
            }
        }
        return answer;
    }

    private boolean isValidParentheses(final String s) {

        if (s.charAt(0) == ']' || s.charAt(0) == '}' || s.charAt(0) == ')') {
            return false;
        }
        final Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (!stack.isEmpty() && compareParenthesis(stack.peek(), ch)) {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        return stack.isEmpty();
    }

    private boolean compareParenthesis(final char ch1, final char ch2) {
        return ch1 == '(' && ch2 == ')'
                || ch1 == '[' && ch2 == ']'
                || ch1 == '{' && ch2 == '}';
    }

    private String rotate(final String s) {
        return s.substring(1) + s.charAt(0);
    }
}