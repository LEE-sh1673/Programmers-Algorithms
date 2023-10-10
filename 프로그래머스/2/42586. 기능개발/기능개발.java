import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class FeatureDevelopment {

    private static final int MAX_PROCESS = 100;

    private final int[] count;

    private final Queue<Integer> queue;

    public FeatureDevelopment() {
        count = new int[MAX_PROCESS + 1];
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
        FeatureDevelopment featDevelopment = new FeatureDevelopment();
        return featDevelopment.sol(progresses, speeds);
    }
}