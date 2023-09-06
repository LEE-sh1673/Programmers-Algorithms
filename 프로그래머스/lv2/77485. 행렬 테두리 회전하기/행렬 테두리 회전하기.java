import java.util.ArrayList;
import java.util.List;

class Solution {
    public static int queryMatrix(int[][] matrix, int[] query) {

        for (int i = 0; i < query.length; i++) {
            query[i] -= 1;
        }

        int tmp = matrix[query[0]][query[1]];
        int minElem = tmp;

        for (int i = query[0]; i < query[2]; i++) {
            matrix[i][query[1]] = matrix[i+1][query[1]];
            minElem = Math.min(minElem, matrix[i+1][query[1]]);
        }
        for (int i = query[1]; i < query[3]; i++) {
            matrix[query[2]][i] = matrix[query[2]][i+1];
            minElem = Math.min(minElem, matrix[query[2]][i+1]);
        }
        for (int i = query[2]; i > query[0]; i--) {
            matrix[i][query[3]] = matrix[i-1][query[3]];
            minElem = Math.min(minElem, matrix[i-1][query[3]]);
        }
        for (int i = query[3]; i > query[1]; i--) {
            matrix[query[0]][i] = matrix[query[0]][i-1];
            minElem = Math.min(minElem, matrix[query[0]][i-1]);
        }
        matrix[query[0]][query[1]+1] = tmp;
        return minElem;
    }
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] matrix = new int[rows][columns];

        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= columns; j++) {
                matrix[i-1][j-1] = columns * (i-1) + j;
            }
        }

        for (int i = 0; i < queries.length; i++) {
            answer[i] = queryMatrix(matrix, queries[i]);
        }
        return answer;
    }
}