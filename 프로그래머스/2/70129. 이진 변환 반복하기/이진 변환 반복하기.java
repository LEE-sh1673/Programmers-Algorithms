class Solution {
    public int[] solution(final String s) {
        int[] answer = new int[2];
        String current = s;

        while (!current.equals("1")) {
            final String zeros = current.replace("1", "");
            current = Integer.toBinaryString(current.length() - zeros.length());
            answer[1] += zeros.length();
            answer[0]++;
        }
        return answer;
    }
}