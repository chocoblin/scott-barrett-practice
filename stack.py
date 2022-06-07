class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
        print("\n")

    def push(self, value):
        new_node = Node(value)
        
        if self.top:
            new_node.next = self.top
        
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height==0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height-=1
            return temp

my_Stack = Stack(9)
my_Stack.print_stack()

my_Stack.push(8)
my_Stack.print_stack()

my_Stack.pop()
my_Stack.print_stack()