class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        int numsConvert = 0;
        int numsZeroRemoved = 0;
        String copy = s;
        
        while (true) {
            String numsZero = copy.replace("1", "");
            copy = Integer.toString(copy.length() - numsZero.length(), 2);
            
            numsZeroRemoved += numsZero.length();
            numsConvert++;
            
            if ("1".equals(copy)) {
                break;
            }
        }
        return new int[] { numsConvert, numsZeroRemoved };
    }
}