import java.util.*;
import java.util.stream.*;

import static java.util.stream.Collectors.*;


class Solution {
    public int solution(String[][] clothes) {
        /*
            (A+1)*(B+1)-1 을 구현
         */
        return Arrays.stream(clothes)
                .collect(Collectors.groupingBy(p -> p[1], Collectors.counting()))
                .values()
                .stream()
                .reduce(1L, (total, count) -> total * (count + 1))
                .intValue() - 1;
    }
}