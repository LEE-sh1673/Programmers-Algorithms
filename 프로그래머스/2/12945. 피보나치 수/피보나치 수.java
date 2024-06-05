class Solution {
    private int fibonacci(final int n) {
        if (n < 2) {
            return n;
        }
        int a = 0;
        int b = 1;

        for (int i = 1; i < n; i++) {
            int tmp = a;
            a = b;
            b = (tmp + b) % 1234567;
        }
        return b;
    }

    public int solution(int n) {
        return fibonacci(n);
    }
}