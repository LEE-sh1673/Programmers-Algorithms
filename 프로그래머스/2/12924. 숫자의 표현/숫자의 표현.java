class Solution {
public int solution(int n) {
        int answer = 0;

        for (int i = 1; i <= n; i++) {
            int total = i;

            for (int j = i+1; j <= n; j++) {
                total += j;

                if (total >= n) {
                    if (total == n) {
                        answer++;
                    }
                    break;
                }
            }
        }
        return answer + 1;
    }
}