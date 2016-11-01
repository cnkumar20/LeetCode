class TreeTraversal {


    public void preorder(Tree root) {
        if(root==null) return;
        System.out.println(root.data);
        inorder(root.left);
        inorder(root.right);
    }
}