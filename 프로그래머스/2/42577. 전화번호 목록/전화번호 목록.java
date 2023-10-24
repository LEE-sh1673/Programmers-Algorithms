import java.util.*;
import java.util.stream.*;


class Solution {
    public boolean solution(String[] phone_book) {
        
        Map<String, Integer> numberSet = new HashMap<>();
        
        for(String number : phone_book) {
            numberSet.put(number, 1);
        }
        
        
        for(String phone_number : phone_book) {
            
            StringBuilder sb = new StringBuilder();
            
            for (int i = 0; i < phone_number.length(); i++) {
                
                sb.append(phone_number.charAt(i));
                
                if (!sb.toString().equals(phone_number) && numberSet.containsKey(sb.toString())) {
                    return false;
                }
            }            
        }
        return true;
    }
}