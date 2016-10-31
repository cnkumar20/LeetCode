/**
 * Created by dexter on 10/28/16.
 */

public class BinaryTree {
    public static class TreeNode {
        int val;
        TreeNode left = null;
        TreeNode right = null;
        TreeNode(int x) {
            val = x;
        }
    }
     public static boolean isBinaryTree(TreeNode root) {
        if(root.left == null & root.right == null){
            return true;
        }

        boolean left =  isBinaryTree(root.left);
        boolean right = isBinaryTree(root.right);

        if(root.left == null & root.val <= root.right.val) {
            return (left&right);
        }

        else if(root.right == null & (root.val >= root.left.val)) {
            return (left&right);
        }
        else if((root.left != null & root.right != null) & root.val >= root.left.val & root.val <= root.right.val) {
            return (left&right);
        }
        else return false;

    }

    public static void main(String[] args) {
        TreeNode ip = new TreeNode(4);
        ip.left = new TreeNode(6);
        ip.right = new TreeNode(5);
        System.out.println(isBinaryTree(ip));
}}
