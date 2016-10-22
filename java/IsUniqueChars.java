/**
 * Created by dexter on 10/22/16.
 */
public class IsUniqueChars {

    public static boolean isUnique(String input){
            if(input.length()>128) return false;
            boolean[] check = new boolean[128];
            for(char c : input.toCharArray()) {
                if(check[c]) return false;
                check[c]=true;
            }
            return true;
    }
    public static void main() {
        String[] input = {"Kumar","sucheta","awesome"};
        for(String in : input){
            System.out.print(isUnique(in));
        }
    }
}
