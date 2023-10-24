import java.util.*;
import java.util.stream.*;


class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        for (int[] size: sizes) {
            if (size[0] < size[1]) {
                int tmp = size[0];
                size[0] = size[1];
                size[1] = tmp;
            }
        }
        
        int max = Arrays.stream(sizes)
            .map(size -> size[0])
            .collect(Collectors.summarizingInt(Integer::intValue))
            .getMax();
        
        int min = Arrays.stream(sizes)
            .map(size -> size[1])
            .collect(Collectors.summarizingInt(Integer::intValue))
            .getMax();
    
        
        return max * min;
    }
}