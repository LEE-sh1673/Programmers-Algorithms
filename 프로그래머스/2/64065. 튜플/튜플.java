import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


class Solution {
    
    public int[] solution(final String s) {
        final String[] keywords = extractKeywords(s);
        final Group[] groups = new Group[keywords.length];

        for (int i = 0; i < groups.length; i++) {
            groups[i] = new Group(keywords[i].split(","));
        }

        Arrays.sort(groups);
        
        final Set<Integer> total = Arrays.stream(groups)
                .flatMap(group ->  group.numbers.stream())
                .collect(Collectors.toCollection(LinkedHashSet::new));
        
        return total.stream().mapToInt(i -> i).toArray();
    }

    private static String[] extractKeywords(final String s) {
        return s
                .substring(1, s.length() - 1)
                .replace("{", "")
                .replace("},", " ")
                .replace("}", "")
                .split(" ");
    }

    static class Group implements Comparable<Group> {
        private final List<Integer> numbers;

        public Group(final String[] numbers) {
            this.numbers = Arrays.stream(numbers)
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
        }

        @Override
        public int compareTo(final Group other) {
            return this.numbers.size() - other.numbers.size();
        }
    }
}