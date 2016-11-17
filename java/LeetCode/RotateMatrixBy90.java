package LeetCode;

import java.util.Arrays;

/**
 * Created by dexter on 10/25/16.
 */
public class RotateMatrixBy90 {
    public static int[][] rotate(int[][] matrix,int n) {
        for(int layer=0;layer<n/2;layer++){
            int first = layer;
            int last = n - layer - 1;
            for(int i=first;i<last;i++) {
                int offset = i-first;
                //save top
                int top = matrix[first][i];

                matrix[first][i] = matrix[last-offset][first];

                matrix[last-offset][first] = matrix[last][last-offset];

                matrix[last][last-offset] = matrix[i][last];

                matrix[i][last] = top;
             }
        }
        return matrix;
    }


    public static void main(String[] args) {
        int[][] a = new int[][]{{1,2,3,4},{2,3,2,5},{5,2,3,1},{6,3,4,2}};

        System.out.println("Before Rotating");

        System.out.println(Arrays.deepToString(a));

        System.out.println("After Rotating :");

        System.out.println(Arrays.deepToString(rotate(a,4)));
    }

}
