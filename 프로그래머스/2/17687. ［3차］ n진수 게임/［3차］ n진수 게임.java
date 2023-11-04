import java.util.*;
import java.util.stream.*;


class Solution {
    
    private static final String[] BASE = "0123456789ABCDEF".split("");
    
    public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();
        
        answer.append("0");
        for (int i = 1; i < m*t; i++) {
            answer.append(conv(i, n));
        }
        
        String tmp = answer.toString().substring(p-1);
        String s = "";
        
        for (int i = 0; i < tmp.length(); i += m) {
            s += tmp.charAt(i);   
        }
        return s.substring(0, t);
    }
    
    
    private String conv(final int number, final int base) {
        int q = number / base;
        int r = number % base;
        
        if (q == 0) {
            return BASE[r];
        } else {
            return conv(q, base) + BASE[r];
        }
    }
}