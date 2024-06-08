import java.util.*;


class Solution {
    
    public int solution(int k, int[] tangerine) {
        final Map<Integer, Integer> countByKind = new HashMap<>();

        for (int ti : tangerine) {
            countByKind.put(ti, countByKind.getOrDefault(ti, 0) + 1);
        }

        int total = 0;
        int answer = 0;

        List<Integer> kinds = new ArrayList<>(countByKind.keySet());
        Collections.sort(kinds, (o1, o2) -> countByKind.get(o2) - countByKind.get(o1));

        for (int kind : kinds) {
            total += countByKind.get(kind);
            answer++;

            if (total >= k) {
                break;
            }
        }
        return answer;

    }
}