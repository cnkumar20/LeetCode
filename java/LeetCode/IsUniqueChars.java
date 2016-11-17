package LeetCode;

/**
 * Created by dexter on 10/22/16.
 */
public class IsUniqueChars {

    public static boolean isUnique_1(String input){
            if(input.length()>128) return false;
            boolean[] check = new boolean[128];
            for(char c : input.toCharArray()) {
                if(check[c]) return false;
                check[c]=true;
            }
            return true;
    }

    public static boolean isUnique_2(String input){
        if(input.length()>128)return false;
        int checker =0;
        for(char c : input.toCharArray()){
            int val = c - 'a';
            if((checker & (1 << val)) > 0) return false;
            checker |= (1<<val);
        }
        return true;
    }


    public static void main(String[] args) {
        String[] input = {"Kumar","sucheta","awesome"};
        for(String in : input){
            System.out.print("Algorithm 1 : "+isUnique_1(in)+" Algorithm 2 :"+isUnique_2(in));
        }
    }
}
