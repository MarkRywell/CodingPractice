package DSA.Tree;

public class Node {
    int data;
    Node left;
    Node right;

    Node(int data, Node left, Node right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }

    public int getData() {
        return this.data;
    }

    public Node getLeft() {
        return this.left;
    }

    public Node getRight() {
        return this.right;
    }

    static int findSum(Node head) {
        if(head == null) return 0;
        return head.getData() + findSum(head.getLeft()) + findSum(head.getRight());
    }
}
