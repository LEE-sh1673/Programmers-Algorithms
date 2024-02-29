import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] periods = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < periods.length; i++) {
            periods[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(periods);

        int answer = 0;
        for (int i = 0; i < periods.length; i++) {
            answer += periods[i] * (n - i);
        }
        System.out.println(answer);
        br.close();
    }
}