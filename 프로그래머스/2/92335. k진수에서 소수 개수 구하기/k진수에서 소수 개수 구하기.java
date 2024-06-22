import java.util.*;


class Solution {
    public int solution(int n, int k) {
        String number = conv(n, k);
        int answer = 0;
        
        for (String num : number.split("0")) {
            if (!num.isBlank()) {
                long t = Long.valueOf(num, 10);
                
                if (isPrime(t)) {
                    answer++;
                }
            }
        }
        return answer;
    }
    
    private String conv(int n, int k) {
        StringBuilder sb = new StringBuilder();
        
        while (n != 0) {
            sb.append(String.valueOf(n % k));
            n /= k;
        }
        return sb.reverse().toString();
    }
    
    private boolean isPrime(long number) {
        if (number <= 1) {
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}