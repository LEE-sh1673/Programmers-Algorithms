import java.util.LinkedList;
import java.util.Queue;

public class MazeEscape {

    private final int[] dirX = new int[]{-1, 1, 0, 0};
    private final int[] dirY = new int[]{0, 0, 1, -1};

    private final String[][] maze;


    private final int[] startPoint;

    private final int[] leverPoint;

    private final int[] endPoint;
    
    private boolean[][] visited;

    private final int xLen;

    private final int yLen;

    private static class Node {
        int x;
        int y;

        int cnt;

        public Node(final int x, final int y, final int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }


    public MazeEscape(final String[] maps) {
        this.xLen = maps.length;
        this.yLen = maps[0].length();
        this.maze = new String[xLen][yLen];
        this.visited = new boolean[xLen][yLen];
        this.startPoint = new int[2];
        this.leverPoint = new int[2];
        this.endPoint = new int[2];
        mapMaze(maps);
    }

    private void mapMaze(final String[] maps) {
        for (int i = 0; i < xLen; i++) {
            for (int j = 0; j < yLen; j++) {
                maze[i][j] = maps[i].substring(j, j + 1);
                visited[i][j] = false;

                if ("S".equals(maze[i][j])) {
                    startPoint[0] = i;
                    startPoint[1] = j;
                } else if ("L".equals(maze[i][j])) {
                    leverPoint[0] = i;
                    leverPoint[1] = j;
                } else if ("E".equals(maze[i][j])) {
                    endPoint[0] = i;
                    endPoint[1] = j;
                }
            }
        }
    }

    public int bfs(final int[] start, final int[] end) {
        String destination = maze[end[0]][end[1]];
        Queue<Node> queue = new LinkedList<>();

        queue.offer(new Node(start[0], start[1], 0));
        visited = new boolean[xLen][yLen];
        visited[start[0]][start[1]] = true;

        while (!queue.isEmpty()) {
            Node now = queue.poll();

            for (int i = 0; i < dirX.length; i++) {
                int nextX = now.x + dirX[i];
                int nextY = now.y + dirY[i];

                if (isValidBoundary(nextX, nextY)) {
                    if (destination.equals(maze[nextX][nextY])) {
                        return now.cnt + 1;
                    }
                    if (!visited[nextX][nextY]) {
                        visited[nextX][nextY] = true;
                        queue.offer(new Node(nextX, nextY, now.cnt + 1));
                    }
                }
            }
        }
        return -1;
    }


    public int sol() {
        int toLever = bfs(startPoint, leverPoint);
        int toEnd = bfs(leverPoint, endPoint);

        if (toLever == -1 || toEnd == -1) {
            return -1;
        }
        return toLever + toEnd;
    }

    private boolean isValidBoundary(final int x, final int y) {
        return isValidRange(x, y) && !"X".equals(maze[x][y]);
    }

    private boolean isValidRange(final int x, final int y) {
        return x >= 0 && x < xLen && y >= 0 && y < yLen;
    }
}


class Solution {
    public int solution(String[] maps) {
        MazeEscape mazeEscape = new MazeEscape(maps);
        return mazeEscape.sol();
    }
}