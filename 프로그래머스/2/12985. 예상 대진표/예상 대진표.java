class Solution
{
    public int solution(int n, int a, int b) {
        if (a == b) {
            return 0;
        }
        return 1 + solution(n, (a + 1) / 2, (b + 1) / 2);
    }
}