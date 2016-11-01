class TreeTraversal {


    public static void preorder(Tree root) {
        if(root==null) return;
        System.out.println(root.data);
        preorder(root.left);
        preorder(root.right);
    }

    public static void inorder(Tree root) {
    if(root==null) return;
        inorder(root.left);
        System.out.println(root.data);
        inorder(root.right);
    }

    public static void postorder(Tree root) {
        if(root==null) return;

        postorder(root.left);
        postorder(root.right);
        System.out.println(root.data);
    }

    public static void main(String[] args) {
        Tree a = new Tree(1);
        inorder(a);
        preorder(a);
    }

}