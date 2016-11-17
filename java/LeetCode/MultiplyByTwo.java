package LeetCode;

/**
 * Created by dexter on 10/25/16.
 */
public class MultiplyByTwo {
    public static void main(String[] args) {
        int num = 2;
        for(int i=0;i<8;i++) {
            num = num << 1;
            System.out.println(num);
        }
    }
}
