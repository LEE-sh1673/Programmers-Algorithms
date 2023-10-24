class Solution {
    
    private static int answer = 0;
    
    private static int r = 0;
    
    public void dfs(int[] numbers, int number, int index) {
        
        if (index == numbers.length) {
            if (number == r) {
                answer++;
            }
        } else {
            dfs(numbers, number - numbers[index], index + 1);
            dfs(numbers, number + numbers[index], index + 1);
        }
    }
    
    public int solution(int[] numbers, int target) {
        r = target;
        dfs(numbers, 0, 0);
        return answer;
    }
}