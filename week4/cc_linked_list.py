class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def prepend(self, value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
            print("Head Node created:", self.head.value)
            return

        new_node.next=self.head
        self.head=new_node
        print("Prepended new Head Node with value:", self.head.value)
        print("Node following Head is:", self.head.next.value)


llist=LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")