import java.util.*;
import java.util.stream.*;


class Solution {
    public int solution(String[][] clothes) {  
        Map<String, Long> t = Arrays.stream(clothes)
            .map(Cloth::new)
            .collect(Collectors.groupingBy(
                Cloth::getType,
                Collectors.counting()
            ));

        long t2 = t.values().stream()
            .reduce(1L, (total, countByType) -> total * (countByType + 1));
  
        return (int) t2 - 1;
    }
    
    private static class Cloth {
        
        private final String name;
        
        private final String type;
        
        Cloth(final String[] cloth) {
            this.name = cloth[0];
            this.type = cloth[1];
        }
        
        public String getType() {
            return type;
        }
    }
}