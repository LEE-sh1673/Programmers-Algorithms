class Solution {

    // public int solution(int k, int[][] dungeons) {
    //     DungeonCostCalculator calculator 
    //         = new DungeonCostCalculator(dungeons);
    //     return calculator.calculate(k);
    // }
    
    public int solution(int k, int[][] dungeons) {
        DungeonTravelSimulator simulator = new DungeonTravelSimulator(dungeons);
        return simulator.getMaximumTravels(k);
    }
    
    private static class DungeonTravelSimulator {

        private static int maximumTravels = 0;

        private final int[] requires;
        private final int[] costs;
        private final boolean[] visited;

        public DungeonTravelSimulator(final int[][] dungeons) {
            this.requires = new int[dungeons.length];
            this.costs = new int[dungeons.length];
            this.visited = new boolean[dungeons.length];

            for (int i = 0; i < dungeons.length; i++) {
                this.requires[i] = dungeons[i][0];
                this.costs[i] = dungeons[i][1];
            }
        }

        public int getMaximumTravels(final int k) {
            simulate(0, k);
            return maximumTravels;
        }

        private void simulate(int count, int cost) {
            for (int i = 0; i < requires.length; i++) {
                if (!visited[i] && cost >= requires[i]) {
                    visited[i] = true;
                    simulate(count + 1, cost - costs[i]);
                    visited[i] = false;
                }
            }
            maximumTravels = Math.max(maximumTravels, count);
        }
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