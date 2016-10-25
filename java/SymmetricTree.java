/**
 * Created by dexter on 10/24/16.
 */
public class SymmetricTree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }
    public boolean isSymmetric(TreeNode root) {
        if(root==null) {
            return true;
        }
        return isSymmetric(root.left,root.right);
    }

    public boolean isSymmetric(TreeNode lNode, TreeNode rNode) {
        if(rNode==null && lNode==null) return true;
        if(rNode==null) return false;
        if(lNode==null) return false;

        return lNode.val == rNode.val && isSymmetric(lNode.left,rNode.right) && isSymmetric(lNode.right,rNode.left);
    }
}
