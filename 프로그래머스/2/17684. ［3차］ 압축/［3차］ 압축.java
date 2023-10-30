import java.util.*;
import java.util.stream.*;


class Solution {
    public int[] solution(String msg) {
        Compressor compressor = new Compressor();
        return compressor.compress(msg);
    }
    
    static class Compressor {
        
        private static final List<String> DICT
            = IntStream.rangeClosed('A', 'Z')
                .mapToObj(Character::toString)
                .collect(Collectors.toList());
        
        public int[] compress(final String msg) {
            List<Integer> indexes = new ArrayList<>();
            
            for (int i = 0; i < msg.length(); i++) {
                StringBuilder w = new StringBuilder(String.valueOf(msg.charAt(i)));
       
                if (i == msg.length() - 1) {
                    indexes.add(DICT.indexOf(w.toString()) + 1);
                    break;
                }
                
                String c = String.valueOf(msg.charAt(i + 1));

                // 사전에 w+c가 있다면
                while (DICT.contains(w + c)) {
                    w.append(c);
                    i++;

                    if (i == msg.length() - 1 || c.equals("")) {
                        c = "";
                        break;
                    }
                    c = String.valueOf(msg.charAt(i + 1));
                }
                
                if (!DICT.contains(w + c)) {
                    DICT.add(w + c);
                }
                int x = DICT.indexOf(w.toString());
                
                if (x != -1) {
                    indexes.add(x + 1);
                }

                // c 에 들어온 문자가 마지막글자면 종료 
                if (i == msg.length() - 1 && !c.equals("")) {
                    indexes.add(DICT.indexOf(c) + 1);
                }
            }
            return indexes.stream()
                .mapToInt(i -> i)
                .toArray();
        }
    }
    
    // 1. 사전에 영문 대문자를 등록 
    // 2. 영문 대문자 문자열 msg를 입력받는다.
    // 3. LZW 압축을 수행한다.
        // 3.1. 현재 단어가 사전에 존재하지 않을 때까지 문자열을 합친다.
        // 3.2. 사전에 존재하는 최대 길이 문자열의 색인 번호를 추가한다.
            // 3.3. 문자열에 끝에 도달한 경우 추가하지 않고 종료한다.
        // 3.3. 존재하지 않는 문자열을 사전에 추가한다.
    
    // A B AB ABA BA BAB ABAB
    // A -> 1, AB -> 27
    // B -> 2, BA -> 28
    // AB -> 27, ABA -> 29
    // ABA -> 29, ABAB -> 30
    // BA -> 28, BAB -> 31
    // BAB -> 31, BABA -> 32
    // ABAB -> 30, NONE
    // return [1, 2, 27, 29, 28, 31, 30]
}