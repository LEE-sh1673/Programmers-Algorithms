import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.function.BiPredicate;


public class LRUCache<K, V> extends LinkedHashMap<K, V> {

    private final int cacheSize;
    private final BiPredicate<Map<K, V>, Map.Entry<K, V>> condition;

    private LRUCache(
        final int cacheSize, 
        final BiPredicate<Map<K, V>, Map.Entry<K, V>> condition
    ) {
        super(cacheSize, 0.75f, true);
        this.cacheSize = cacheSize;
        this.condition = condition;
    }

    @Override
    protected boolean removeEldestEntry(final Entry<K, V> eldest) {
        return condition.test(this, eldest);
    }

    public static <K, V> LRUCache<K, V> newInstance(final int cacheSize) {
        return new LRUCache<>(
            cacheSize, 
            (map, eldestEntry) -> map.size() > cacheSize
        );
    }
}


class Solution {
    public int solution(int cacheSize, String[] cities) {
        LRUCache<String, String> cache = LRUCache.newInstance(cacheSize);
        int answer = 0;
        
        for (final String city : cities) {
            final String name = city.toLowerCase();
            
            if (cache.containsKey(name)) {
                answer++;        
            } else {
                answer += 5;
            }
            cache.put(name, name);
        }
        return answer;
    }
}