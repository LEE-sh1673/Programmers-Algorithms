import java.util.*;


class Solution {
    
    public int solution(int[] elements) {
        final int[] newElements = new int[2 * elements.length];

        for (int i = 0; i < newElements.length; i++) {
            newElements[i] = elements[i % elements.length];
        }

        final Set<Integer> numbers = new HashSet<>();

        for (int i = 1; i <= elements.length; i++) {
            for (int j = 0; j < elements.length; j++) {
                int[] sliceNumbers = Arrays.copyOfRange(newElements, j, j + i);
                int sum = 0;

                for (int number : sliceNumbers) {
                    sum += number;
                }
                numbers.add(sum);
            }
        }
        return numbers.size();
    }
}