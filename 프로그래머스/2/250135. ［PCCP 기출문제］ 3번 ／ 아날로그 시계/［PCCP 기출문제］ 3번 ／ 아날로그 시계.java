/*
- 초침이 시침/분침과 겹치는 경우 알림이 울린다.
- 초침은 1분 내로 시침과 분침을 모두 만나게 된다.
- 단순히 생각해보면 1분마다 2번씩 알람이 울리므로, 1시간에 120번이 울리고, 12시간에 1440, 하루에 2880번이 울리게 되는 것이다.

- 그러나 예외의 경우도 생각해봐야 한다.
    - 시간이 h시 59분 -> (h+1)시 0분으로 갈때는 초침과 분침이 만나지 않는다. 하루를 기준으로 이러한 경우는 총 24번 발생하므로 이를 제외한다. (24)
    - 시간이 11시 59분 -> 12시, 또는 23시 59분 -> 0시로 갈때는 초침과 시침이 만나지 않는다. 이를 제외한다.  (2)
    - 0시 정각, 12시 정각에 초침과 시침, 분침이 모두 겹칠 때는 알람이 한 번만 울린다. 따라서 이를 제외한다. (2)
- 따라서 하루에 알림은 총 2880 - (24 + 2 + 2) = 2852번 울리게 된다.
- 다만 시작 시간과 끝나는 시간이 유동적이기 때문에,
    <0:0:0~h2:m2:s2 알림 횟수> - <0:0:0~h1:m1:s1 알림 횟수> 를 구하면 된다.

[회전 각도]
- 초침은 60초에 360도를 회전한다. -> s * 360 / 60 -> s*6
- 분침은 60분에 360도를 회전한다. -> m * 360 / 60 -> m*6
- 시침은 12시간에 360도를 회전한다. -> h * 360 / 12 -> h*30

- 분침은 초침의 현재 위치에 따라 위치가 결정된다. 따라서
    (m*6 + s*360/60/60) = m*6 + s*0.1
- 시침은 분침과 초침의 현재 위치에 따라 위치가 결정된다. 따라서
    (h*30 + m*360/60/12 + s*360/60/12/60) -> (h*30 + m*0.5 + s*30) 
    
정리하면 다음과 같다.
- 초침 = 6s
- 분침 = 6m
- 시침 = 30h + 0.5m + 30s
*/
class Solution {
    
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        final Degree d1 = new Degree(h1, m1, s1);
        final Degree d2 = new Degree(h2, m2, s2);
        final int answer = DegreeCalculator.calculate(d1, d2);
        return answer;
    }
    
    static class DegreeCalculator {
        static int calculate(final Degree d1, final Degree d2) {
            final int c1 = d1.count();
            final int c2 = d2.count();
            return d1.isOverlap() ? c2 - c1 + 1 : c2 - c1;
        }
    }
    
    static class Degree {
        
        private double h;
        private double m;
        private double s;
        
        private int hours;
        private int minutes;
        private int seconds;
        
        Degree(final int h, final int m, final int s) {
            this.hours = h;
            this.minutes = m;
            this.seconds = s;
            this.h = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360; 
            this.m = m * 6 + s * 0.1;
            this.s = s * 6;
        }
        
        int count() {
            int count = -1;
            
            if (s >= m) {
                count++;
            }
            if (s >= h) {
                count++;
            }
            count += (hours*60+minutes) * 2;
            count -= hours;
            
            if (hours >= 12) {
                count -= 2;
            }
            return count;
        }
        
        boolean isOverlap() {
            return s == h || s == m;
        }
    }
}