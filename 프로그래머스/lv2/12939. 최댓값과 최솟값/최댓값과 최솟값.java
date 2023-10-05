import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;


class Solution {
    public String solution(String s) {
        List<Integer> k = List.of(s.split(" ")).stream()
            .map(t -> Integer.parseInt(t))
            .sorted()
            .collect(Collectors.toList());

        return k.get(0) + " " + k.get(k.size()-1);
    }
}