import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int m;
    static int numberOfPair;
    static int[][] friends;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new boolean[n + 1];

        friends = new int[m][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            friends[i][0] = Integer.parseInt(st.nextToken());
            friends[i][1] = Integer.parseInt(st.nextToken());
        }

        // 가능한 조합 수 탐색
        findPairs(0, 0);

        int answer = numberOfPair * 2;

        if (answer < n) {
            answer++;
        }
        System.out.println(answer);
    }

    private static void findPairs(final int idx, final int count) {
        if (idx >= m) {
            numberOfPair = Math.max(numberOfPair, count);
            return;
        }
        if (visited[friends[idx][0]] || visited[friends[idx][1]]) {
            findPairs(idx + 1, count);
            return;
        }
        visited[friends[idx][0]] = true;
        visited[friends[idx][1]] = true;
        findPairs(idx + 1, count + 1);

        visited[friends[idx][0]] = false;
        visited[friends[idx][1]] = false;
        findPairs(idx + 1, count);
    }
}
