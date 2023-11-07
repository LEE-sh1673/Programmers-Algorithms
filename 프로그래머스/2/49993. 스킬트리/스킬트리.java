import java.util.*;


class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for (final String skill_tree : skill_trees) {
            boolean canMake = true;
            
            Queue<String> queue = new LinkedList<>();
            
            for (final String s : skill.split("")) {
                queue.add(s);
            }
            
            for (String s : skill_tree.split("")) {
                if (skill.contains(s) && !s.equals(queue.remove())) {
                    canMake = false;
                    break;
                }
            }
            
            if (canMake) {
                answer++;
            }
        }
        return answer;
    }
}