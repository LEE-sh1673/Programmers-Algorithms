class Solution {
    
    private static int answer = 0;
    private static int count = 0;
    private static String[] ALPHABETS = new String[] { "A", "E", "I", "O", "U" };
    
    public int solution(final String word) {
        dfs("", word);
        return answer;
    }
    
    private void dfs(final String word, final String target) {
        if (target.equals(word)) {
            answer = count;
        }
        
        if (word.length() > 5) {
            return;
        }
        
        count++;
        
        for (int i = 0; i < 5; i++) {
            dfs(word + ALPHABETS[i], target);
        }
    }
}