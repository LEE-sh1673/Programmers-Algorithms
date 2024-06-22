import java.util.*;
import java.util.stream.*;


class Solution {

    public boolean solution(String[] phone_book) {
        Set<String> phoneNumbers = new HashSet<>(Arrays.asList(phone_book));

        for (final String phone_number : phone_book) {
            for (int i = 1; i < phone_number.length(); i++) {
                if (phoneNumbers.contains(phone_number.substring(0, i))) {
                    return false;
                }
            }
        }
        return true;
    }
}