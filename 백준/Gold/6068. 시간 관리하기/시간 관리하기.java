import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    
    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int n = Integer.parseInt(br.readLine());
        final Schedule[] schedules = new Schedule[n];

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            schedules[i] = new Schedule(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }
        Arrays.sort(schedules);
        System.out.println(getRemainsTime(schedules));
        br.close();
    }

    private static int getRemainsTime(final Schedule[] schedules) {
        int answer = Integer.MAX_VALUE;
        int time = 0;

        for (final Schedule schedule : schedules) {
            time += schedule.requiredTime;
            answer = Math.min(answer, schedule.finishedTime - time);
        }
        if (answer < 0) {
            return -1;
        }
        return answer;
    }

    static class Schedule implements Comparable<Schedule> {
        private final int requiredTime;
        private final int finishedTime;

        public Schedule(int requiredTime, int finishedTime) {
            this.requiredTime = requiredTime;
            this.finishedTime = finishedTime;
        }

        @Override
        public int compareTo(final Schedule other) {
            if (this.finishedTime > other.finishedTime) {
                return 1;
            } else if (this.finishedTime < other.finishedTime) {
                return -1;
            }
            return 0;
        }
    }
}