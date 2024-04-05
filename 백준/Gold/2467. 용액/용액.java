import java.util.*;
import java.io.*;

public class Main
{
	public static void main(String[] args) throws IOException {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		final int N = Integer.parseInt(br.readLine());
		final int[] nums = new int[N];
		
		final StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		for (int i = 0; i < N; i++) {
		    nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int start = 0;
		int end = N-1;
		int min_blending = Math.abs(nums[start] + nums[end]);
		
		final int[] answer = new int[] {nums[start], nums[end]};
		
		while (start < end) {
		    final int blending = nums[start] + nums[end];
		    
		    if (min_blending > Math.abs(blending)) {
		        min_blending = Math.abs(blending);
		        answer[0] = nums[start];
		        answer[1] = nums[end];
		    }
		    
		    if (blending < 0) {
		        start++;
		    } else {
		        end--;
		    }
		}
		System.out.println(answer[0] + " " + answer[1]);
	}
}