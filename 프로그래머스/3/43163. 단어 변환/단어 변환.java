import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


class Solution {
    
    private static final Map<String, List<String>> graph = new HashMap<>();

    public int solution(String begin, String target, String[] words) {
        for (String word : words) {
            graph.put(word, getOneLetterMatchWords(word, words));
        }
        graph.put(begin, getOneLetterMatchWords(begin, words));
        return dfs(begin, target, List.of());
    }
    
    private int dfs(
        final String word, 
        final String target, 
        final List<String> visited
    ) {
        if (word.equals(target)) {
            return visited.size();
        }
        if (visited.contains(word)) {
            return 0;
        }

        List<Integer> results = new ArrayList<>();

        for (String w : graph.get(word)) {
            List<String> trace = new ArrayList<>(visited);
            trace.add(word);

            int r = dfs(w, target, trace);

            if (r != 0) {
                results.add(r);
            }
        }
        return results.stream()
            .mapToInt(Integer::intValue)
            .min()
            .orElse(0);
    }

    private List<String> getOneLetterMatchWords(
        final String target, 
        final String[] words
    ) {
        return Arrays.stream(words)
            .filter(word -> equalsOneLetter(target, word))
            .collect(Collectors.toList());
    }

    private boolean equalsOneLetter(final String target, final String word) {
        return !target.equals(word) && countDifferentLetters(target, word) == 1;
    }

    private int countDifferentLetters(final String target, final String word) {
        return (int)IntStream.range(0, target.length())
            .filter(i -> target.charAt(i) != word.charAt(i))
            .count();
    }
}