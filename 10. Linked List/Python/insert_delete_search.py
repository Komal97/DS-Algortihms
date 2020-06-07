'''
1) create linked list
2) insert at beginning. middle, end
3) delete at beginning. middle, end
4) search a key in linked list (recursively and iteratively)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    # find length of linked list
    def length_of_ll(self):
        length = 0
        temp = self.head
        while(temp != None):
            temp = temp.link
            length+=1
        return length

    # insert node at beginning
    def inserAtBeg(self, data):
        n = Node(data)
        n.link = self.head
        self.head = n

    # delete node at beginning
    def deleteAtBeg(self):
        if self.head == None:
            return
        temp = self.head
        self.head = self.head.link
        temp = None

    # insert node at end
    def insertAtTail(self, data):
        if self.head == None:
            self.head = Node(data)
            return 

        temp = self.head
        while(temp.link != None):
            temp = temp.link
        n = Node(data)
        temp.link = n
        n.link = None

    # delete node at end
    def deleteAtTail(self):
        if self.head == None:
            return
        temp = self.head
        prev = None
        while temp.link != None:
            prev = temp
            temp = temp.link
        temp = None
        prev.link = None
        
    # insert node in middle
    def insertInMiddle(self, data, position):
        if (self.head==None or position==0):
            inserAtBeg(data)
        elif (position > self.length_of_ll()):
            insertAtTail(data)
        else:
            jump = 1
            temp = self.head
            while(jump <= position-1):
                temp = temp.link
                jump += 1
            n = Node(data)
            n.link = temp.link
            temp.link = n

    # delete node in middle
    def deleteInMiddle(self, position):
        if (self.head == None or position == 0):
            deleteAtBeg()
        if (position > self.length_of_ll()):
            deleteAtTail()
        else:
            jump = 1
            temp = self.head
            while(jump <= position-1):
                temp = temp.link
                jump +=1
            ptr = temp.link
            temp.link = ptr.link
            ptr = None

    # search a node iteratively
    def searchIterative(self, key):
        temp = self.head
        while (temp != None):
            if temp.data == key:
                return True
            temp = temp.link
        return False

    # seach a node recursively
    def searchRecursive(self, head, key):
        if head == None:
            return False
        elif head.data == key:
            return True
        else:
            return self.searchRecursive(head.link, key)

    # print linked list
    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "->", end = "")
            temp = temp.link
        print()

ll = LinkedList()
ll.inserAtBeg(5)
ll.inserAtBeg(4)
ll.inserAtBeg(2)
ll.inserAtBeg(1)
ll.insertAtTail(6)
ll.insertInMiddle(3, 2)
ll.printList()
print(ll.searchIterative(5))
print(ll.searchIterative(15))
print(ll.searchRecursive(ll.head, 5))
print(ll.searchRecursive(ll.head, 15))
ll.deleteAtBeg()
ll.printList()
ll.deleteAtTail()
ll.printList()
ll.deleteInMiddle(2)
ll.printList()