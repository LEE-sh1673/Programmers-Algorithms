import java.util.*;

class Solution {

    public int solution(int[][] maps) {
        final int n = maps.length;
        final int m = maps[0].length;
        final Queue<Position> que = new LinkedList<>();
        final boolean[][] visited = new boolean[n][m];

        final int[] dx = new int[]{1, -1, 0, 0};
        final int[] dy = new int[]{0, 0, 1, -1};

        // 시작 위치 처리
        visited[0][0] = true;
        que.add(new Position(0, 0, 1));

        int answer = Integer.MAX_VALUE;

        while (!que.isEmpty()) {
            final Position pos = que.poll();

            if (pos.x == n - 1 && pos.y == m - 1) {
                answer = Math.min(answer, pos.cnt);
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = pos.x + dx[i];
                int ny = pos.y + dy[i];

                if (nx > n - 1 || nx < 0 || ny > m - 1 || ny < 0) {
                    continue;
                }

                if (!visited[nx][ny] && maps[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    que.add(new Position(nx, ny, pos.cnt + 1));
                }
            }
        }
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }

    private static class Position {
        private final int x;
        private final int y;
        private final int cnt;

        public Position(final int x, final int y, final int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}