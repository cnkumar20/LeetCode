/**
 * Created by dexter on 11/5/16.
 */
public class MultithreadingDemo extends Thread {
    @Override
    public void run() {
        try {
            System.out.println("Thread "+Thread.currentThread().getId() + " is running");
        }
        catch(Exception e) {
            System.out.println("Exception is caught!!");
        }
    }
}
