import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class FeatureDevelopment {

    private static final int MAX_PROCESS = 100;

    private final Queue<Integer> queue;

    public FeatureDevelopment() {
        queue = new LinkedList<>();
    }
    
    public int calculateRemainDate(final int progress, final int speed) {
        double remain = (100 - progress) / (double) speed;
        return (int) Math.ceil(remain);
    }

    public int[] sol(int[] progresses, int[] speeds) {
        List<Integer> dates = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            int remainDate = calculateRemainDate(progresses[i], speeds[i]);

            if (!queue.isEmpty() && queue.peek() < remainDate) {
                dates.add(queue.size());
                queue.clear();
            }
            queue.offer(remainDate);
        }
        dates.add(queue.size());
        queue.clear();

        return dates.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}


class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        final Queue<Integer> days = new LinkedList<>();
        final List<Integer> deploys = new ArrayList<>();

        for (int i = 0; i < progresses.length; i++) {
            int remainDays = calculateRemainDays(progresses[i], speeds[i]);

            if (!days.isEmpty() && days.peek() < remainDays) {
                deploys.add(days.size());
                days.clear();
            }
            days.offer(remainDays);
        }

        if (!days.isEmpty()) {
            deploys.add(days.size());
            days.clear();
        }
        return deploys.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }

    private int calculateRemainDays(final int progress, final int speed) {
        return (int) Math.ceil((100.0 - progress) / speed);
    }

}