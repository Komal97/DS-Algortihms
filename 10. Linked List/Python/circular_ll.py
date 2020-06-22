class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    # function to find length of list
    def length(self):
        temp = self.head
        count = 0
        while(True):
            if self.head == None:
                break
            count += 1
            temp = temp.link
            if temp == self.head: break
        return count

    # function to insert node 
    def insert(self, data, pos):
        if pos < 0 or pos > self.length():
            return
        
        # insert at beginning
        if pos == 0:
            # if empty list
            if self.head == None:
                self.head = Node(data)
                self.head.link = self.head
            # if list is not empty
            else:    
                temp = self.head
                while(temp.link != self.head):
                    temp = temp.link
                n = Node(data)
                n.link = self.head
                temp.link = n
                self.head = n 
        # insert in middle or end
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.link
            n = Node(data)
            n.link = temp.link
            temp.link = n
    
    # function to delete node
    def delete(self, pos):
        if pos<=0 or pos>self.length() or self.head == None:
            return
        temp = self.head
        # delete from beginning
        if pos == 1:
            while(temp.link != self.head):
                temp = temp.link
            # if one node present
            if self.head == temp:
                self.head = None
            # if more than one node present
            else:
                temp.link = self.head.link
                self.head = None
                self.head = temp.link
        # delete from middle or end 
        else:
            for i in range(pos-2):
                temp = temp.link
            ptr = temp.link
            temp.link = ptr.link
            ptr = None

    # function to print list
    def printList(self):
        if self.head == None:
            return 
        temp = self.head
        while(True):
            print(temp.data, '->', end = " ")
            temp = temp.link
            if temp == self.head: break
        print()

ll = CircularLinkedList()
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    ll.insert(arr[i], i)
ll.printList()
num = int(input())
ll.delete(num)
ll.printList()