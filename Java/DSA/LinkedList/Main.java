public class Main {
    public static void main(String[] args) {

        Node node4 = new Node(8, null);
        Node node3 = new Node(7, node4);
        Node node2 = new Node(1, node3);
        Node head = new Node(3, node2);

        System.out.println(Node.getCount(head));
    }
}

