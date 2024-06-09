import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public int solution(final String a, final String b) {
        List<Integer> zeros = new ArrayList<>();
        List<Integer> ones = new ArrayList<>();

        for (int i = 0; i < a.length(); i++) {
            char ch = a.charAt(i);

            if (ch != b.charAt(i)) {
                if (ch == '0') {
                    zeros.add(i);
                } else {
                    ones.add(i);
                }
            }
        }
        return Math.max(zeros.size(), ones.size());
    }

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final Main main = new Main();
        final int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String[] ab = br.readLine().split(" ");
            System.out.println(main.solution(ab[0], ab[1]));
        }
    }
}
