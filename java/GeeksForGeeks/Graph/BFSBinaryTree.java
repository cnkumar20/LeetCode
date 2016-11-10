package GeeksForGeeks.Graph;

import DataStructure.*;

import java.util.ArrayDeque;
import java.util.Queue;

/**
 * Created by dexter on 11/6/16.
 */
public class BFSBinaryTree {
    TreeNode node;


    BFSBinaryTree(TreeNode node) {
        this.node = node;
    }


    public boolean breadthFirstSearch(int a) {
        if (node == null) return false;

        return breadthFirstSearch(a, node);

    }


    public boolean breadthFirstSearch(int num,TreeNode node) {
        Queue<TreeNode> temp = new ArrayDeque<>();

        temp.add(node);

        while(!temp.isEmpty()) {
            TreeNode tempNode = temp.poll();
            if(tempNode.a == num) {
                return true;
            }
            if(tempNode.left != null) {
                temp.add(tempNode.left);
            }

            if(tempNode.right != null) {
                temp.add(tempNode.right);
            }
        }
        return false;
    }

}
