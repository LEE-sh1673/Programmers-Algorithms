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
    // boolean solution(String s) {
    //     CorrectParenthesis parenthesis = new CorrectParenthesis(s);
    //     return parenthesis.isCorrectOrder();
    // }
    
    boolean solution(String s) {
        int count = 0;
        
        for (int i = 0; i < s.length(); i++) {
            count += s.charAt(i) == '(' ? 1 : -1;
            
            if (count < 0) {
                return false;
            }
        }
        return count == 0;
    }
}