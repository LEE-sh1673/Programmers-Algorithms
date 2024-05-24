import java.util.*;
import java.io.*;

public class Main
{
    private static int[] dx = new int[] { 0, -1, -1, -1, 0, 1, 1, 1 };
    private static int[] dy = new int[] { -1, -1, 0, 1, 1, 1, 0, -1 };
    
    private static int n;
    private static int m;
    private static int[][] board;
    private static boolean[][] removed;
    
    private static void move(final List<Pair> clouds, final Pair command) {
        
        final int di = command.getX();
        final int steps = command.getY();
        final Set<Pair> moved = new HashSet<>();
        
        for (final Pair cloud : clouds) {
            int nx = (cloud.getX() + dx[di-1] * steps) % n;
            int ny = (cloud.getY() + dy[di-1] * steps) % n;
            
            nx = nx < 0 ? n + nx : nx;
            ny = ny < 0 ? n + ny : ny;
   
            board[nx][ny] += 1;
            removed[nx][ny] = true;
            moved.add(Pair.of(nx, ny));
        }
        
        for (final Pair cloud : moved) {
            int x = cloud.getX();
            int y = cloud.getY();
            int cnt = 0;
            
            for (int i = 1; i < 8; i += 2) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }
                
                if (board[nx][ny] > 0) {
                    cnt++;
                }
            }
            board[x][y] += cnt;
        }
        
        clouds.clear();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                final Pair pair = Pair.of(i, j);
                
                if (!removed[i][j] && board[i][j] >= 2) {
                    board[i][j] -= 2;   
                    clouds.add(pair);
                }
            }
        }
    }
    
	public static void main(String[] args) throws IOException {
	    
	    final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st = new StringTokenizer(br.readLine());
	    
	    n = Integer.parseInt(st.nextToken());
	    m = Integer.parseInt(st.nextToken());
	    board = new int[n][n];
	    
	    for (int i = 0; i < n; i++) {
	        st = new StringTokenizer(br.readLine());
	        
	        for (int j = 0; j < n; j++) {
	            board[i][j] = Integer.parseInt(st.nextToken());
	        }
	    }
	    
	    final List<Pair> clouds = new ArrayList<>();
	    
	    clouds.addAll(List.of(
	        Pair.of(n-2, 0), Pair.of(n-2, 1),
	        Pair.of(n-1, 0), Pair.of(n-1, 1)));
	    
	    final List <Pair> commands = new ArrayList<>();
	    
	    for (int i = 0; i < m; i++) {
	        st = new StringTokenizer(br.readLine(), " ");
	        int d = Integer.parseInt(st.nextToken());
	        int s = Integer.parseInt(st.nextToken());
	        commands.add(Pair.of(d, s));
	    }
	    
	    for (final Pair command : commands) {
	        removed = new boolean[n][n];
	        move(clouds, command);
	    }
	    int total = Arrays.stream(board).flatMapToInt(Arrays::stream).sum();
	    System.out.println(total);
	    br.close();
	}
	
	private static class Pair {
	    
	    final int x;
	    final int y;
	    
	    Pair(final int x, final int y) {
	        this.x = x;
	        this.y = y;
	    }
	    
	    static Pair of(final int x, final int y) {
	        return new Pair(x, y);
	    }
	    
	    int getX() {
	        return x;
	    }
	    
	    int getY() {
	        return y;
	    }
	    
	    @Override
	    public boolean equals(final Object o) {
	        
	        if (this == o) {
	            return true;
	        }
	        
	        if (o == null || !(o instanceof Pair)) {
	            return false;
	        }
	        final Pair other = (Pair) o;
	        return this.x == other.x && this.y == other.y;
	    }
	    
	    @Override
	    public int hashCode() {
	        return Objects.hash(x, y);
	    }
	}
}
