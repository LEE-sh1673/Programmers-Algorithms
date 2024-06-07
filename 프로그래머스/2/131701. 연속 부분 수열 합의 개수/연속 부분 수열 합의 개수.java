import java.util.*;


class Solution {
    
    public int solution(int[] elements) {
        final int[] dp = new int[elements.length];
        final Set<Integer> numbers = new HashSet<>();
        final int n = elements.length;

        for (int len = 1; len <= n; len++) {
            for (int i = 0; i < n; i++) {
                dp[i] += elements[(len + i + 1) % n];
                numbers.add(dp[i]);
            }
        }
        return numbers.size();
    }
}