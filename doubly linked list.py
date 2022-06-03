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
        print(str(self.head.value) + "-" + str(self.tail.value)+"\n")
        #the above line obviously gives errors for no items

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length+=1
        return True

    def pop(self):
        if self.length==0:
            return None
        if self.length==1:          
            self.head = None
            self.tail = None 
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length-=1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length-=1
        return temp

    def get(self, index):
        if index<0 or index>self.length:
            return None
        
        if index<self.length/2:
            temp= self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        if index<0 or index>self.length:
            return False
        if index==self.length:
            return self.append(index, value)
        if index==0:
            return self.prepend(index, value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length+=1
        return True
        


my_doubly_linked_list = DoublyLinkedList(6)
my_doubly_linked_list.print_list()

my_doubly_linked_list.append(7)
my_doubly_linked_list.print_list()

my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()

my_doubly_linked_list.prepend(5)
my_doubly_linked_list.print_list()

my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()

my_doubly_linked_list.append(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(9)
my_doubly_linked_list.append(10)
my_doubly_linked_list.print_list()

print(my_doubly_linked_list.get(3))

my_doubly_linked_list.set_value(4,0)
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(4,10)
my_doubly_linked_list.print_list()