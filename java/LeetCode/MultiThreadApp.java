package LeetCode;

/**
 * Created by dexter on 11/5/16.
 */
public class MultiThreadApp {
    public static void main(String[] args) {
        int n = 8;
        for(int i=0;i<8;i++) {
            MultithreadingDemo mt = new MultithreadingDemo();
            mt.start();
        }
    }
}
