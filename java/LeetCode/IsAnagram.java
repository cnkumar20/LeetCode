package LeetCode;

import java.util.Arrays;

/**
 * Created by dexter on 10/22/16.
 */
public class IsAnagram {

    public static String sortString(String input) {
        char[] charInput = input.toCharArray();
        Arrays.sort(charInput);
        return new String(charInput);


    }
    public static boolean isAnagram(String input1,String input2) {
        return sortString(input1).equals(sortString(input2));

    }

    public static void main(String[] args) throws Exception{
        String[][] input = {{"Kumar","Sucheta"},{"dog","god"}};
        for(String[] in : input) {
            System.out.println(isAnagram(in[0],in[1]));
        }
    }
}
