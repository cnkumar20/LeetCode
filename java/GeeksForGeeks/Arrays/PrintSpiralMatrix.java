package GeeksForGeeks.Arrays;

/**
 * Created by kumar on 11/17/2016.
 */
public class PrintSpiralMatrix {

    public static void printMatrix(int[][] mat, int m, int n) {
        int k = 0, l = 0, i;

        while (k < m && l < n) {
            for (i = l; i < n; i++) {
                System.out.println(mat[k][i]);
            }
            k++;

            for (i = k; i < m; i++) {
                System.out.println(mat[i][n - 1] + " ");
            }
            n--;

            if (k < m) {
                for (i = n - 1; i > l; i--) {
                    System.out.println(mat[m][i] + " ");
                }
            }

            if (l < n) {
                for (i = m - 1; i > k; i--) {
                    System.out.println(mat[i - 1][l] + " ");
                }
            }
        }
    }

    public static void main(String[] args) {
        int[][] a = new int[3][];
        a[0] = new int[] {1, 2, 3, 4, 5, 6};
        a[1] = new int[] {7, 8, 9, 10, 11, 12};
        a[2] = new int[] {13, 14, 15, 16, 17, 18};
        printMatrix(a, 3, 6);
    }

}
