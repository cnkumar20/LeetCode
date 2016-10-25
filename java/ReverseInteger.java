/**
 * Created by dexter on 10/24/16.
 */
public class ReverseInteger {
    public static int reverse(int num) {
        int newValue = 0;
        while(num !=0) {
            newValue = newValue*10+num % 10;
            num = num/10;
        }
        return newValue;
    }

    public static void main(String[] args) {
        System.out.println(reverse(2001));
    }
}


