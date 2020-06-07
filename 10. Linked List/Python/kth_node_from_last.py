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
    
    # find kth element from the last 
    def find_kth_node_from_last(self, k):
        if self.head == None or self.head.link == None:
            return None
     
        fast = self.head       
        slow = self.head
        
        for i in range(k):
            fast = fast.link
            
        while(fast != None):
            slow = slow.link
            fast = fast.link
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
print(ll.find_kth_node_from_last(3))