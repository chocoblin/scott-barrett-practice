from tempfile import tempdir
from sklearn.utils import indexable
from sympy import re


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

    # def set_value(self, value, index):
    #     #check if valid index
    #     if index <0 or index > self.length :
    #         return None
    #     temp = self.head
    #     #this will set temp as the node at given index
    #     for _ in range (index):    
    #         temp = temp.next
    #     temp.value = value
    #     return True

    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



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