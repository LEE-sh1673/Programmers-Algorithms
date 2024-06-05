class Solution {
    
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int br = brown + yellow;

        for (int w = 3; w <= Math.sqrt(br); w++) {
            int h = br / w;

            if ((w - 2) * (h - 2) == yellow) {
                answer[0] = Math.max(w, h);
                answer[1] = Math.min(w, h);
                break;
            }
        }
        return answer;
    }
}