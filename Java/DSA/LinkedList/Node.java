public class Node {
    int data;
    Node next;

    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }

    public int getData() {
        return this.data;
    }

    public Node getNext() {
        return this.next;
    }

    public int getNextData() {
        return this.next.data;
    }

    public static int getCount(Node head) {
        int count = 1;
        Node current = head;
        while(current != null) {
            count++;
            current = current.next;
        }
        return count;
    }
}
