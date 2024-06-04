class CorrectParenthesis {
    
    private static final char LEFT_PARENTHESIS = '(';

    private static final char RIGHT_PARENTHESIS = ')';

    private final String parenthesis;

    public CorrectParenthesis(final String parentheses) {
        this.parenthesis = parentheses;
    }

    boolean isCorrectOrder() {
        int numberOfParenthesis = 0;

        for (int i = 0; i < parenthesis.length(); i++) {
            numberOfParenthesis += getNumberOfParenthesis(parenthesis.charAt(i));
            if (numberOfParenthesis < 0) {
                return false;
            }
        }
        return numberOfParenthesis == 0;
    }

    private int getNumberOfParenthesis(int currentParenthesis) {
        if (currentParenthesis == LEFT_PARENTHESIS) {
            return 1;
        } else if (currentParenthesis == RIGHT_PARENTHESIS) {
            return -1;
        }
        return 0;
    }
}


class Solution {
    boolean solution(final String s) {
        if (s.startsWith(")")) {
            return false;
        }

        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                count++;
            }
            else if (s.charAt(i) == ')') {
                count--;
            }
            if (count < 0) {
                return false;
            }
        }
        return count == 0;
    }
}