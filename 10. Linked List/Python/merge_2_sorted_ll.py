'''
create linked list by user input
merge 2 sorted linked list recursively
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

    # function to merge 2 sorted linked list iteratively
    def merge_iterative(self, a, b):
        if a == None:
            self.head = b
            return
        elif b == None:
            self.head = a
            return 
        
        if a.data <= b.data:
            self.head = a
            a = a.link
        else:
            self.head = b
            b = b.link
            
        c = self.head
        while(a != None and b != None):
            if a.data < b.data:
                c.link = a
                a = a.link
            else:
                c.link = b
                b = b.link
            c = c.link
        if a:
            c.link = a
        if b:
            c.link = b
       
    # function to merge 2 sorted linked list recursively
    def merge_ll(self, a, b):
        def merge(a, b):
            if a == None:
                return b

            elif b == None:
                return a
            
            if (a.data < b.data):
                c = a
                c.link = merge(a.link, b)
            else:
                c = b
                c.link = merge(a, b.link)
            return c
        self.head = merge(a, b)

    # print linked list
    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "->", end = "")
            temp = temp.link
        print()

ll1 = LinkedList()
ll1.build_ll()
ll1.print_list()

ll2 = LinkedList()
ll2.build_ll()
ll2.print_list()

# ll3 = LinkedList()
# ll3.merge_ll(ll1.head, ll2.head)
# ll3.print_list()

ll4 = LinkedList()
ll4.merge_iterative(ll1.head, ll2.head)
ll4.print_list()


