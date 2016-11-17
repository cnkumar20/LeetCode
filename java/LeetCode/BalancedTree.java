package LeetCode;

/**
 * Created by dexter on 10/26/16.
 */
public class BalancedTree {
    public static int getHeight(SameTree.TreeNode root) {
        if(root==null) return 0;
        return Math.max(getHeight(root.left),getHeight(root.right))+1;
    }

    public boolean isBalanced(SameTree.TreeNode root) {
        if(root==null) return true;
        int heightDiff = getHeight(root.left) - getHeight(root.right);
        if(Math.abs(heightDiff)>1) return false;
        else return isBalanced(root.left) && isBalanced(root.right);
    }
}
