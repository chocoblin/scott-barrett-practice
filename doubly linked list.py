class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self, value):
        new_node = Node (value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print(str(self.head.value) + str(self.tail.value)+"\n")

    def append(self, value):
        new_node = Node(value)
        #case 1 empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #case 2 at least 1 element present
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length+=1
        return True

    def pop(self):
        #case 1 no item
        if self.length==0:
            return None
        #case 2 if originally only 1 element
        if self.length==1:          
            self.head = None
            self.tail = None 
        #case 3 2 or more
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length-=1
        return temp.value

my_doubly_linked_list = DoublyLinkedList(6)
my_doubly_linked_list.print_list()

my_doubly_linked_list.append(7)
my_doubly_linked_list.print_list()

my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()