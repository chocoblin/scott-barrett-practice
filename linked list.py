from tempfile import TemporaryDirectory, tempdir


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("\n")

    def append(self, value):
        new_node = Node(value)
        #case 1 empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #case 2 atleast 1 element present
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length+=1
        return True

    # def pop(self):
    #     #case 1 empty list
    #     if self.head is None:
    #         print("No element in LL")
    #     #case 2 1 element present
    #     elif self.head.next is None:

    #         print("no. popped is " + str(self.head.value))
    #         self.head = None
    #         self.tail = None
    #         self.length-=1
    #     #case 3 more than 1 element present
    #     else:
    #         temp = self.head
    #         pre = self.head
    #         while temp.next is not None:
    #             pre = temp
    #             temp = temp.next
    #         self.tail = pre
    #         self.tail.next = None
    #         self.length-=1
    #         print("no. popped is " + str(temp.value))

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self,value):
        new_node = Node(value)
        #case 1 empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #case 2 elements present
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True        

    # def pop_first(self):
    #     #case 1 e=mpty list
    #     if self.head is None:
    #         print("no item in LL")
    #     #case 2 1 item
    #     elif self.head.next is None:
    #         print ( "no. popped is " + str(self.head.value))
    #         self.head = None
    #         self.tail = None
    #         self.length-=1
    #     #case 3 2 or more items
    #     else:
    #         print ("no. popped is " + str(self.head.value))
    #         temp = self.head
    #         self.head = self.head.next
    #         temp.next = None
    #         self.length-=1

    def pop_first(self):
        if self.length==0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1
        if self.length==0:
            self.tail = None
        return temp

    def get (self, index):
        #check if valid index
        if index <0 or index > self.length :
            return None
        temp = self.head
        #this will set temp as the node at given index
        for _ in range (index):    
            temp = temp.next
        return temp

    # def set_value(self, index, value):
    #     #check if valid index
    #     if index <0 or index > self.length :
    #         return None
    #     temp = self.head
    #     #this will set temp as the node at given index
    #     for _ in range (index):    
    #         temp = temp.next
    #     temp.value = value
    #     return True

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index ==0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        
        #multiple elements
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        return True
    
    def remove(self, index):
        if index < 0 or index >self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == (self.length-1):
            return self.pop()
        
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        return True

   
my_linked_list = LinkedList(3)
my_linked_list.print_list()

my_linked_list.append(4)
my_linked_list.print_list() 

my_linked_list.pop()
my_linked_list.print_list()

my_linked_list.prepend(4)
my_linked_list.print_list()

my_linked_list.pop_first()
my_linked_list.print_list()

my_linked_list.set_value(0,7)
my_linked_list.print_list()

my_linked_list.append(8)
my_linked_list.append(9)
my_linked_list.prepend(6)
my_linked_list.print_list()

my_linked_list.insert(2,1)
my_linked_list.print_list()

my_linked_list.remove(2)
my_linked_list.print_list()