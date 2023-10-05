import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;


class Solution {
    
// 테스트 1 효율성에서 시간 초과
//     public int solution(int[] A, int[] B) {
//         Arrays.sort(A);
//         Integer[] wrapped = Arrays.stream(B)
//             .boxed()
//             .toArray(Integer[]::new);
//         Arrays.sort(wrapped, Collections.reverseOrder());
   
//         int answer = 0;
        
//         for (int i = 0; i < A.length; i++) {
//             answer += (A[i] * wrapped[i]);
//         }
//         return answer;
//     }
    
// Arrays.sort() 보다 더 빠른 알고리즘을 사용
    public int solution(final int[] A, final int[] B) {
        final PriorityQueue<Integer> a = new PriorityQueue<>();
        final PriorityQueue<Integer> b = new PriorityQueue<>(Collections.reverseOrder());
        int answer = 0;
        
        for (int i = 0; i < A.length; i++) {
            a.add(A[i]);
            b.add(B[i]);
        }
        
        while (!a.isEmpty()) {
            answer += a.poll() * b.poll();
        }
        return answer;
    }
}