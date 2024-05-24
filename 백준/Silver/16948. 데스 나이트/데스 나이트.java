import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Objects;
import java.util.StringTokenizer;

public class Main {

    static int[] dx = new int[]{-2, -2, 0, 0, 2, 2};
    static int[] dy = new int[]{-1, 1, -2, 2, -1, 1};

    static int n;
    static int r1;
    static int c1;
    static int r2;
    static int c2;

    static boolean[][] visited;
    static Deque<Pair> que = new LinkedList<>();
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        visited = new boolean[n][n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        r2 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        solve();
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
        br.close();
    }

    private static void solve() {
        final Pair source = Pair.of(r1, c1);
        final Pair destination = Pair.of(r2, c2);

        que.offer(source);
        visited[r1][c1] = true;

        while (!que.isEmpty()) {
            final Pair pair = que.poll();

            if (pair.equals(destination)) {
                answer = Math.min(answer, pair.dist);
                continue;
            }

            for (int i = 0; i < 6; i++) {
                int nx = pair.x + dx[i];
                int ny = pair.y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }
                if (visited[nx][ny]) {
                    continue;
                }
                visited[nx][ny] = true;
                que.offer(Pair.of(nx, ny, pair.dist + 1));
            }
        }
    }

    private static class Pair {

        final int x;
        final int y;
        final int dist;

        Pair(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        static Pair of(int x, int y) {
            return new Pair(x, y, 0);
        }

        static Pair of(int x, int y, int dist) {
            return new Pair(x, y, dist);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}
