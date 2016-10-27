import java.util.ArrayList;
import java.util.HashMap;

/**
 *             0 1
 *             / \
 *           1 2  3  -1
 *           / \ / \
 *        2 4 05 06 7 -2
 *
 *
 *
 * Created by dexter on 10/26/16.
 */
public class VerticalOrderBinaryTree {
    static class Tree {
        int val;
        Tree left;
        Tree right;

        Tree(int a) {
            val = a;
            left=null;
            right =null;
        }
    }

    public static void printTree(Tree inputTree) {
        HashMap<Integer,ArrayList> a = new HashMap<>();

        mapNodes(a,inputTree,0);

        for(ArrayList<Integer> ite : a.values()) {
            for(int num : ite) {
                System.out.print(num+" ");
            }
            System.out.println();
        }
    }

    public static void mapNodes(HashMap<Integer,ArrayList> track, Tree input, int l) {
        if(input == null) return;

        if(!track.containsKey(l))  {
            track.put(l,new ArrayList<Integer>());
        }

        track.get(l).add(input.val);
        mapNodes(track,input.left,l+1);
        mapNodes(track,input.right,l-1);
    }

    public static void main(String[] args) {
        Tree input = new Tree(1);
        input.left = new Tree(2);
        input.right = new Tree(3);
        input.left.left = new Tree(4);
        input.left.right = new Tree(5);
        input.right.left = new Tree(6);
        input.right.right = new Tree(7);
        input.left.right.left = new Tree(8);

        printTree(input);

    }
}
