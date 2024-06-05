class Solution {
    public int solution(int n) {
        int answer = 0;
        int nCount = countOnes(n);

        for (int k = n+1; k < 2*n; k++) {
            if (nCount == countOnes(k)) {
                answer = k;
                break;
            }
        }
        return answer;
    }

    private int countOnes(final int number) {
        return Integer.toBinaryString(number)
                .replace("0", "")
                .length();
    }
}