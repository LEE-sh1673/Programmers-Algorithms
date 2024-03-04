import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Result {

    public static int numberOfCoins(final int money, final int[] coins) {
        int numberOfCoins = 0;
        int currentMoney = money;

        for (int i = coins.length - 1; i >= 0; i--) {
            if (currentMoney >= coins[i]) {
                numberOfCoins += currentMoney / coins[i];
                currentMoney %= coins[i];
            }
        }
        return numberOfCoins;
    }
}


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] coins = new int[n];

        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        System.out.println(Result.numberOfCoins(k, coins));
        br.close();
    }

}
