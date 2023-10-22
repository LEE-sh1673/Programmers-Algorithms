class Solution {
    
    public static boolean visited[];
    
    public static int ans = 0;

    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        dfs(k, dungeons, 0);
        return ans;
    }
    
    public static void dfs(int cost, int[][] dungeons, int cnt){
        for(int i = 0; i < dungeons.length; i++) {
            
            if(!visited[i] && dungeons[i][0] <= cost) {
                visited[i] = true;
                dfs(cost - dungeons[i][1], dungeons, cnt+1);
                visited[i] = false;
            }
        }
        ans = Math.max(ans, cnt);
    }
}