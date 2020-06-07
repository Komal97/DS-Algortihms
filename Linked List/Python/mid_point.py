'''
create linked list by user input
find middle element in linked list using runner's method
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
    
    # find middle element using runner's method
    def find_mid(self):
        if self.head == None or self.head.link == None:
            return self.head
       
      # fast = self.head.next  #if middle elemet in even length array is one one
        fast = self.head       #if middle elemet in even length array is second one
        slow = self.head
        
        while(fast != None and fast.link != None):
            slow = slow.link
            fast = fast.link.link
        return slow.data

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
print("Middle element", ll.find_mid())