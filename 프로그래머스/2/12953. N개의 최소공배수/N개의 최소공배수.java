class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];

        for (int i = 1; i < arr.length; i++) {
            answer = lcm(answer, arr[i]);
        }
        return answer;
    }

    private int lcm(final int a, final int b) {
        return (a*b) / gcd(a, b);
    }

    private int gcd(final int a, final int b) {
        int a1 = Math.max(a, b);
        int b1 = Math.min(a, b);

        while (b1 != 0) {
            int n = a1 % b1;
            a1 = b1;
            b1 = n;
        }
        return a1;
    }
}