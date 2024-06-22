class Solution {

    private static int N;
    private static int key;
    private static int answer;
    private static int[] nums;
    private static boolean[] visited;

    public int solution(int[] numbers, int target) {
        N = numbers.length;
        key = target;
        nums = numbers;
        visited = new boolean[N];
        dfs(0, 0);
        return answer;
    }

    private void dfs(int idx, int total) {
        if (idx >= N) {
            if (total == key) {
                answer++;
            }
            return;
        }
        dfs(idx + 1, total + nums[idx]);
        dfs(idx + 1, total - nums[idx]);
    }
}