'''
create linked list by user input
reverse linked list by pointers (recursively and iteratively)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    # insert node at end
    def insert_at_tail(self, data):
        if self.head == None:
            self.head = Node(data)
            return 

        temp = self.head
        while(temp.link != None):
            temp = temp.link
        n = Node(data)
        temp.link = n
        n.link = None
    
    # build user input linked list 
    def build_ll(self):
        data = int(input())
        while(data!=-1):
            self.insert_at_tail(data)
            data = int(input())
    
    # reverse linked list iteratively by reversing pointers 
    def reverse_iterative(self):
        p = None
        c = self.head

        while c!= None:
            n = c.link
            c.link = p
            p = c
            c = n
        self.head = p

    # reverse linked list recursively by reversing pointers
    def reverse_recursive(self):
        def reverse(head):
            if head.link == None or head == None:
                return head
            smallhead = reverse(head.link)
            c = head
            c.link.link = c 
            c.link = None
            return smallhead
        self.head = reverse(self.head)

    # print linked list
    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "->", end = "")
            temp = temp.link
        print()

ll = LinkedList()
ll.build_ll()
ll.print_list()
ll.reverse_iterative()
ll.print_list()
ll.reverse_recursive()
ll.print_list()