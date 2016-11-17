package LeetCode;

/**
 * Created by dexter on 10/24/16.
 */
public class MaximumDepthOfBinaryTree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) {
            val = x;
        }
    }

    public int maxDepth(TreeNode root) {
        if(root==null) {
            return 0;
        }
        int iRightDepth = maxDepth(root.right);
        int iLeftDepth = maxDepth(root.left);
        return (iRightDepth>iLeftDepth)?iRightDepth+1:iLeftDepth+1;
    }
}
