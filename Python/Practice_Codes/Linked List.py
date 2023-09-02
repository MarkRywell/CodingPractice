
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head

        while printval is not None:
            print(printval.data)
            printval = printval.next


nodeA = LinkedList()
nodeA.head = Node(6)

nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

nodeA.listprint()
