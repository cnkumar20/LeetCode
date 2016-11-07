package GeeksForGeeks.Graph;

import GeeksForGeeks.DataStructure.TreeNode;

/**
 * Created by dexter on 11/6/16.
 */
public class DFSBinaryTree {
    TreeNode root;


    DFSBinaryTree(TreeNode root) {
        this.root = root;
    }


    public boolean DFS(int a) {
        return dfs(a,TreeNode root);
    }

    public boolean dfs(int a ,TreeNode root) {

        if(root.a== a) {
            return true;
        }

        if(root.left == null) return false;


        return dfs(a,root.left) || dfs (a,root.right);

    }





}
