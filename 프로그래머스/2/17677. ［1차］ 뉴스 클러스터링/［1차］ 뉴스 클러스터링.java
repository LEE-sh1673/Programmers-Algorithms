// J(A, B)
// = 교집합 크기 / 합집합 크기
// J(x, x)
// = 1 (두 집합이 모두 공집합일 경우)
//
// J(A, B)
// - 교집합: min(count_A, count_B)
// - 합집합: max(count_A, count_B)
//
// e.g.s
// A = {1, 1, 2, 2, 3}
// B = {1, 2, 2, 4, 5}
// A n B = {1, 2, 2}
// A u B = {1, 1, 2, 2, 3, 4, 5}
// 3 / 7 ~ 0.42

// 1. 자카드 유사도 집합 만들기
// - 각 집합을 소문자/대문자로 변환
// - 크기를 2만큼 각각 슬라이싱 한다.
// - 슬라이싱된 각 요소를 검사한다.
//  - 영문자로된 글짜 쌍이 아니면 버린다.

// 2. 자카드 유사도 교집합 만들기
// - A 집합의 카운트를 구한다.
// - B 집합의 카운트를 구한다.
// - A[i] == B[i] 인 경우를 구한다.
//  - min(A[i].count, B[i].count)

// 2. 자카드 유사도 합집합 만들기
// - A 집합의 카운트를 구한다.
// - B 집합의 카운트를 구한다.
// - 모든 집합을 합친다.
// - A[i] == B[i] 인 경우를 아래를 수행
//  - max(A[i].count, B[i].count)

// J(A, B)
// 1. 유사도 집합 만들기
// 2. 교집합 만들기
// 3. 합집합 만들기
// 4. 교집합 // 합집합

import java.util.*;
import java.util.stream.*;
import java.util.regex.*;
import java.util.function.*;


class Solution {
    public int solution(String str1, String str2) {        
        JaccardCoefficientMeter meter = new JaccardCoefficientMeter(str1, str2);
        return meter.meter();
    }
    
    private static class JaccardCoefficientMeter {

        private static final int MULTIPLIER = 65536;
        
        private final Map<String, Long> s1Keywords;
        private final Map<String, Long> s2Keywords;

        public JaccardCoefficientMeter(final String str1, final String str2) {
            this.s1Keywords = extractKeywords(str1.toUpperCase());
            this.s2Keywords = extractKeywords(str2.toUpperCase());
        }

        private Map<String, Long> extractKeywords(final String word) {
            return IntStream.range(0, word.length() - 1)
                    .mapToObj(i -> word.substring(i, i + 2))
                    .filter(AlphabetMatcher::matches)
                    .collect(Collectors.groupingBy(w -> w, Collectors.counting()));
        }

        public int meter() {
            Integer numberOfInteraction = interaction();
            Integer numberOfUnion = union();

            if (numberOfInteraction.equals(numberOfUnion) && numberOfUnion.equals(0)) {
                return MULTIPLIER;
            }
            double coefficientRatio = numberOfInteraction.doubleValue() / numberOfUnion.doubleValue();
            return (int) (coefficientRatio * MULTIPLIER);
        }

        private Integer interaction() {
            return s1Keywords.keySet().stream()
                    .filter(s2Keywords::containsKey)
                    .map(word -> Math.min(s1Keywords.get(word), s2Keywords.get(word)))
                    .mapToInt(Long::intValue)
                    .sum();
        }

        private Integer union() {
            return mergeKeywords().values().stream()
                    .mapToInt(Long::intValue)
                    .sum();
        }

        private Map<String, Long> mergeKeywords() {
            final Map<String, Long> keywords = new HashMap<>(s2Keywords);
            s1Keywords.forEach((key, value) ->
                    keywords.put(key, Math.max(value, s2Keywords.getOrDefault(key, 0L)))
            );
            return keywords;
        }

        private static final class AlphabetMatcher {

            private static final Pattern ALPHABET_PATTERN = Pattern.compile("[a-zA-Z]+");

            public static boolean matches(final String word) {
                return ALPHABET_PATTERN.matcher(word).matches();
            }
        }
    }
}

class JaccardCoefficientMeter {
    
    private static final Pattern ALPHA_PATTERN = Pattern.compile("^[a-zA-Z]+$");
    
    private static final Integer MULTIPLIER = Character.MAX_VALUE + 1;
    
    private final Map<String, Long> s1;
    private final Map<String, Long> s2;
    
    JaccardCoefficientMeter(final String s1, final String s2) {
        this.s1 = mapSet(s1.toLowerCase());
        this.s2 = mapSet(s2.toLowerCase());
    }
    
    private Map<String, Long> mapSet(final String s) {
        return IntStream.range(0, s.length() - 1)
            .mapToObj((i) -> s.substring(i, i+2))
            .filter((word) -> ALPHA_PATTERN.matcher(word).matches())
            .collect(Collectors.groupingBy(w -> w, Collectors.counting()));
    }
    
    public int meter() {
        final Integer intersection = interact();
        final Integer union = union();
        
        if (intersection.equals(union) && union.equals(0)) {
            return MULTIPLIER;
        }
        return (int) (intersection.doubleValue() / union.doubleValue() * MULTIPLIER);
    }
    
    private Integer interact() {
       return s1.entrySet().stream()
                .filter(entry -> s2.containsKey(entry.getKey()))
                .map(entry -> Math.min(entry.getValue(), s2.get(entry.getKey())))
                .mapToInt(Long::intValue)
                .sum();
    }
    
    private Integer union() {
        Map<String, Long> copiedWords = new HashMap<>(s2);
        s1.forEach((key, value) -> 
            copiedWords.put(key, Math.max(value, s2.getOrDefault(key, 0L)))
        );
        return copiedWords.values().stream()
                .mapToInt(Long::intValue)
                .sum();
    }
}