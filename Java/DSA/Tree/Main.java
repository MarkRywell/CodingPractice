package DSA.Tree;

public class Main {
    public static void main(String[] args) {

        Node node4 = new Node(5, null, null);
        Node node3 = new Node(6, null, null);
        Node node2 = new Node(3, node4, node3);
        Node node1 = new Node(4, null, null);
        Node root = new Node(2, node2, node1);

        System.out.println(Node.findSum(root));

    }
}

