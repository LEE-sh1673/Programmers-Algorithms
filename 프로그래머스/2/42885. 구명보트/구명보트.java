import java.util.*;


class Solution {
    
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int numberOfPeople = people.length;
        int numberOfPair = 0;

        int start = 0;
        int end = numberOfPeople - 1;

        while (start < end) {
            int weight = people[start] + people[end];

            if (weight <= limit) {
                numberOfPair++;
                start++;
            } 
            end--;
        }
        return numberOfPeople - numberOfPair;
    }
}