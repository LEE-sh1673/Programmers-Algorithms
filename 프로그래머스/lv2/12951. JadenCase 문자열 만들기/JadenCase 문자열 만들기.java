import java.util.StringTokenizer;


class Solution {
    public String solution(String s) {
        String answer = "";
        final StringTokenizer st = new StringTokenizer(s, " ", true);
        
        while (st.hasMoreTokens()) {
            answer += capitalize(st.nextToken());
        }
        return answer;
    }
    
    private String capitalize(final String s) {
        if (s.isBlank()) {
            return s;
        }
        return s.substring(0, 1).toUpperCase() 
            + s.substring(1).toLowerCase();
    }
}