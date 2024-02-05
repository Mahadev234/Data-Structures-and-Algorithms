class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    # Create a new node
    def __init__(self, value):
        new_node = Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
my_linked_list = LinkedList(4)

my_linked_list.print_list()