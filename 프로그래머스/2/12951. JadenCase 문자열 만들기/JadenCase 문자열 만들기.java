import java.util.StringTokenizer;

import static java.lang.Character.isDigit;
import static java.lang.Character.isUpperCase;
import static java.lang.Character.toLowerCase;
import static java.lang.Character.toUpperCase;

import java.util.StringTokenizer;

class Solution {
    
    public String solution(final String s) {
        final StringTokenizer st = new StringTokenizer(s, " ", true);
        final StringBuilder sb = new StringBuilder();

        while (st.hasMoreTokens()) {
            sb.append(toJadenCase(st.nextToken()));
        }
        return sb.toString();
    }
    
    private String toJadenCase(final String s) {
        final StringBuilder sb = new StringBuilder();
        sb.append(toUpperCase(s.charAt(0)));
        
        for (int i = 1; i < s.length(); i++) {
            sb.append(toLowerCase(s.charAt(i)));
        }
        return sb.toString();
    }
}