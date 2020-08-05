class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class HashTable:
    
    def __init__(self, ds = 7):
        self.__cs = 0                       # current size
        self.__ts = ds                      # table size = default size
        self.__buckets = [None]*self.__ts
        
    # find hash value for a given key
    def __hashFunc(self, key):
        
        ans = 0
        p = 1                               # because 37^0 = 1
        L = len(key)
        for i in range(L):
            ans += ord(key[L-i-1])*p
            p *= 37
            p %= self.__ts                  # this is done to reduce the size of p if p overflow
            ans %= self.__ts                # this is done to reduce the size of ans if ans overflow
        return ans
    
    # increase size of hashtable if loadfactor increases
    def __reshash(self):
        
        # save current bucket 
        oldbucket = self.__buckets
        oldts = self.__ts
        
        # update size and create new bucket with double size
        self.__ts *= 2
        self.__cs = 0 
        self.__buckets = [None]*self.__ts
        
        # read from old bucket and insert in new bucket
        for i in range(oldts):
            temp = oldbucket[i]
            while temp != None:
                self.insert(temp.key, temp.val)
                temp = temp.next
    
    # insert key value in hashtable
    def insert(self, key, value):
        
        i = self.__hashFunc(key)
        
        n = Node(key, value)                # insert at head
        n.next = self.__buckets[i]
        self.__buckets[i] = n
        
        self.__cs += 1
        load_factor = self.__cs/self.__ts
        if load_factor > 0.7:
            self.__reshash()
    
    # return value with given key from hashtable
    def search(self, key):
        
        i = self.__hashFunc(key)
        temp = self.__buckets[i]
        while temp != None:
            if temp.key == key:
                return temp.val
            temp = temp.next
        return None
    
    # delete a key from hashtable
    def delete(self, key):
        i = self.__hashFunc(key)
        temp = self.__buckets[i]
        
        if temp and temp.key == key:
            self.__buckets[i] = temp.next
            del temp
            return
            
        while temp:
            if temp.next and temp.next.key == key:
                ptr = temp.next
                temp.next = ptr.next
                del ptr
                return
            temp = temp.next
    
    # print hashtable
    def printHashTable(self):
        
        for i in range(self.__ts):
            temp = self.__buckets[i]
            print(i, end = ' ===> ')
            while temp != None:
                print(temp.key, '->', temp.val, end = ' ')
                temp = temp.next
            print()
        print()
    
    # return value corresponding to obj[..]
    def __getitem__(self, key):
        return self.search(key)
    
# hashtable of Fruits
h = HashTable()
h.insert('Mango', 30)
h.insert('Apple', 20)
h.insert('Guava', 10)
h.printHashTable()
h.insert('Banana', 50)
h.insert('Chiku', 80)
h.insert('Lichi', 100)
h.printHashTable()
h.delete('Mango')
h.printHashTable()
#print(h.search('Chiku'))
print(h['Chiku'])
