'''
create linked list by user input
detect and remove cycle using floyd cycle detection algorithm
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
    
    # detect cycle
    def detect_cycle(self):
        
        slow = self.head
        fast = self.head
        while fast!=None and fast.link!=None:
            slow = slow.link
            fast = fast.link.link

            if slow == fast:
                return True
        return False

     # detect and remove cycle 
    def detect_and_remove_cycle(self):
        
        slow = self.head
        fast = self.head
		prev = None
        while fast!=None and fast.link!=None:
			prev = slow
            slow = slow.link
            fast = fast.link.link
            if slow == fast:
                break

        if slow == fast:
            slow = self.head
            while slow != fast:
				prev = fast
                fast = fast.link
                slow = slow.link
			prev.link = None

    # print linked list
    def print_list(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "->", end = "")
            temp = temp.link
        print()

ll = LinkedList()
ll.insert_at_tail(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.insert_at_tail(4)
ll.insert_at_tail(5)
ll.print_list()
ll.head.link.link.link.link.link = ll.head.link
print(ll.detect_cycle())
ll.detect_and_remove_cycle()
ll.print_list()

