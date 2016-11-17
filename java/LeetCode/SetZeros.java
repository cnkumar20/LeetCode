package LeetCode;

import java.util.Arrays;

/**
 * Created by dexter on 10/25/16.
 */
public class SetZeros {
    public static int[][] setZeros(int[][] matrix) {
        boolean[] row = new boolean[matrix.length];
        boolean[] column = new boolean[matrix[0].length];

        for(int i=0;i<matrix.length;i++) {
            for(int j=0;j<matrix[0].length;j++) {
                if(matrix[i][j]==0) {
                    row[i] = true;
                    column[j] = true;
                }
            }
        }
        //nullify rows

        for(int i=0;i<row.length;i++) {
            if(row[i]) nullifyRow(matrix,i);
        }

        for(int j=0;j<column.length;j++) {
            if(column[j]) nullifyColumn(matrix,j);
        }

        return matrix;
    }

    public static void nullifyRow(int[][] m, int row) {
        for(int j=0;j<m[0].length;j++) {
            m[row][j] = 0;
        }
    }

    public static void nullifyColumn(int[][] m, int column) {
        for(int j=0;j<m.length;j++) {
            m[j][column] = 0;
        }


    }


    public static void main(String[] args) {
        int[][] a = new int[][]{{1,2,3,0},{2,3,2,5},{5,2,3,1},{6,3,4,2}};
        System.out.println(Arrays.deepToString(setZeros(a)));
    }
}
