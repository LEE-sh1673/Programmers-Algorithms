class Solution {

    public int solution(int k, int[][] dungeons) {
        DungeonCostCalculator calculator 
            = new DungeonCostCalculator(dungeons);
        return calculator.calculate(k);
    }
}


class DungeonCostCalculator {
    
    private static int answer = 0;
    
    private int[][] dungeons;
    
    private boolean[] visited;
    
    DungeonCostCalculator(final int[][] dungeons) {
        this.dungeons = dungeons;
        this.visited = new boolean[dungeons.length];
    }
    
    public int calculate(final int cost) {
        dfs(cost, 0);
        return answer;
    }
    
    private void dfs(int cost, int count) {
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && dungeons[i][0] <= cost) {
                visited[i] = true;
                dfs(cost - dungeons[i][1], count + 1);   
                visited[i] = false;
            }
        }
        answer = Math.max(answer, count);
    }
}