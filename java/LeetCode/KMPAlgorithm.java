package LeetCode;

/**
 * Created by dexter on 10/27/16.
 */
public class KMPAlgorithm {
    public static int[] preProcess(char[] pattern) {
        int i=0,j=-1;

        int ptrnLen = pattern.length;

        int[] b = new int[ptrnLen + 1];

        b[i] = j;

        while(i < ptrnLen) {
            while(j>=0 && pattern[i] != pattern[j]) {
                j = b[j];
            }
            i++;
            j++;
            b[i] = j;
        }
        return b;
    }


    public static int searchSubstring(char[] text, char[] ptrn) {
        int i = 0, j = 0;

        int ptrnLen = ptrn.length;
        int txtLen = text.length;

        int[] b = preProcess(ptrn);

        while (i < txtLen) {
            while (j >= 0 && text[i] != ptrn[j]) {
                j = b[j];
            }
            i++;
            j++;

            if (j == ptrnLen) {
                j = b[j];
                return i - ptrnLen;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        String s = "Kumar is awesome!!";
        String patter = "awes";

        System.out.println("Result : " + searchSubstring(s.toCharArray(),patter.toCharArray()));
    }
}
