class TreeTraversal {


    public void preorder(Tree root) {
        if(root==null) return;
        System.out.println(root.data);
        preorder(root.left);
        preorder(root.right);
    }
    public void inorder(Tree root) {
    if(root==null) return;

    }
}