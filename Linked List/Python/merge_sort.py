'''
merge sort
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

    # function to merge 2 linked list 
    def merge(self, a, b):
        if a == None:
            return b

        elif b == None:
            return a
        
        if (a.data <= b.data):
            c = a
            c.link = self.merge(a.link, b)
        else:
            c = b
            c.link = self.merge(a, b.link)
        return c

    # find middle element using runner's method
    def find_mid(self, head):
        if head == None or head.link == None:
            return head

        fast = head.link     
        slow = head
        
        while(fast != None and fast.link != None):
            slow = slow.link
            fast = fast.link.link
        return slow

    # sorting
    def sort(self, head):
        if head == None or head.link == None:
            return head

        mid = self.find_mid(head)
        a = head
        b = mid.link
        mid.link = None
        a = self.sort(a)
        b = self.sort(b)
        c = self.merge(a,b)
        return c

    # merge sort
    def merge_sort(self):
        self.head = self.sort(self.head)

    # build user input linked list 
    def build_ll(self):
        data = int(input())
        while(data!=-1):
            self.insert_at_tail(data)
            data = int(input())

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
ll.merge_sort()
ll.print_list()



