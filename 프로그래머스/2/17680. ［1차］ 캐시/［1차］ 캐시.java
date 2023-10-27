import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map.Entry;
import java.util.stream.Stream;


class LRUCache extends LinkedHashMap<String, Integer> {

    private static final int CACHE_HIT = 1;
    private static final int CACHE_MISS = 5;

    private final int cacheSize;

    public LRUCache(final int cacheSize) {
        this.cacheSize = cacheSize;
    }

    public int register(final String item) {
        if (isHit(item)) {
            this.remove(item);
            this.put(item, CACHE_HIT);
            return CACHE_HIT;
        }
        this.put(item, CACHE_MISS);
        return CACHE_MISS;
    }

    private boolean isHit(final String item) {
        return this.containsKey(item);
    }

    @Override
    protected boolean removeEldestEntry(final Entry<String, Integer> eldest) {
        return size() > cacheSize;
    }
}


class Solution {
    public int solution(int cacheSize, String[] cities) {
        LRUCache cache = new LRUCache(cacheSize);
        return Stream.of(cities)
                .mapToInt((city) -> cache.register(city.toLowerCase()))
                .sum();
    }
}