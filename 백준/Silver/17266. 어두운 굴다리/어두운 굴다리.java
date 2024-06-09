import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 어두운 굴다리
 */
public class Main {

    // 시간제한 1초 -> O(N^2)은 사용 불가능
    // 굴다리 길이가 N이라고 할때, 최대 높이는 N이다. (1 <= H <= N)
    // 최소 비용을 산출하는 임의의 H를 이분 탐색으로 찾는 과정을 거친다.
    // 1. mid = N//2
    // 2. mid 일때 현재 가로등의 위치에 대입한다.
    // 3.   A. 모든 길을 밝힐 수 있다면, 최소 값을 찾기 위해 end = mid
    //      B. 모든 길을 밝힐 수 없다면, 가능한 범위를 산정하기 위해 start = mid + 1

    static int n;
    static int m;
    static int[] positions;

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        positions = new int[m];

        final StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for (int i = 0; i < m; i++) {
            positions[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = n;

        while (start < end) {
            int height = start + (end - start) / 2;

            if (possible(positions, height)) {
                end = height;
            } else {
                start = height + 1;
            }
        }
        System.out.println(start);
    }

    /*
     * [1 4], h=2 
     * [(-h)1(+h) -- (-h)4(+h)]
     * 
     */
    private static boolean possible(final int[] positions, final int h) {
        int prev = 0;
        for (int position : positions) {
            if (position - h <= prev) {
                prev = position + h;
            } else {
                return false;
            }
        }
        return n - prev <= 0;
    }
}
