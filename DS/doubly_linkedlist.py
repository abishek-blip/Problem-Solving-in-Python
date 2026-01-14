class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    
class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insertStart(self, data):
        newnode = Node(data)

        if(self.head == None):
            self.head = newnode
            return 

        self.head.prev = newnode
        newnode.next = self.head
        self.head = newnode


    def insertEnd(self, data):
        newnode = Node(data)

        if(self.head == None):
            self.head = newnode
            return
        
        temp = self.head
        while (temp.next != None):
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp


    def insertPosition(self, index, data):
        if(index < 0):
            print("Invalid Index")
            return
        
        if (self.head == None):
            if (index == 0):
                self.insertStart(data)
            else:
                print("LinkedList is empty and invalid index")
            return

        if(index == 0):
            self.insertStart(data)
            return
        
        temp = self.head
        count = 0
        newnode = Node(data)

        while (temp != None and count < index - 1):
            temp = temp.next
            count = count + 1

        if (temp == None):
            print("Index out of range")
            return

        if (temp.next == None):
            temp.next = newnode
            newnode.prev = temp
            return
        
        newnode.next = temp.next
        temp.next = newnode
        newnode.prev = temp
        newnode.next.prev = newnode


    def deleteStart(self):
        if (self.head == None):
            print("LinkedList is empty")
            return

        if (self.head.next == None):
            self.head = None
            return
        
        temp = self.head.next
        self.head.next = None
        temp.prev = None
        self.head = temp


    def deleteEnd(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        if (self.head.next == None):
            self.head = None
            return

        temp = self.head
        while temp.next.next != None:
            temp = temp.next

        temp.next.prev = None
        temp.next = None

        
    def deletePosition(self, index):
        if (self.head == None):
            print("LinkedList is empty")
            return
        
        if (index < 0):
            print("Invalid Index")
            return
        
        if (index == 0):
            self.deleteStart()
            return
        
        temp = self.head
        count = 0
        while (temp.next != None and count < index - 1):
            temp = temp.next
            count = count + 1

        if (temp.next == None):
            print("Index out of range")
            return

        if (temp.next.next == None):
            temp.next.prev =None
            temp.next = None
            return
        
        nextnode = temp.next
        temp.next = nextnode.next
        nextnode.next.prev = temp


    def search(self, data):
        if (self.head == None):
            print("LinkedList is empty")
            return
        
        count = 0
        isfound = False
        temp = self.head
        while (temp != None):
            if(temp.data == data):
                print("the value", data,"is found at the index ", count)
                isfound = True
                return
            temp = temp.next
            count = count + 1

        if (isfound == False):
            print("the value", data, "is not found at any index")


    def lengthofthelist(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        count = 0
        temp = self.head
        while (temp != None):
            count = count + 1
            temp = temp.next

        print("Total length of the list is ", count)


    def reverselist(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        nextnode = None
        curr = self.head
        while (curr != None):
            nextnode = curr.prev
            curr.prev = curr.next
            curr.next = nextnode
            curr = curr.prev

        if nextnode != None:
            self.head = nextnode.prev

    
    def displayForward(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        temp = self.head
        print("LinkedList(Forward): None <-", end="")
        while (temp.next != None):
            print(temp.data,"<->", end=" ")
            temp = temp.next

        print(temp.data, "-> None")


    def displayBackward(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        temp = self.head
        while (temp.next != None):
            temp = temp.next

        print("LinkedList(Backward): None <-", end="")
        while (temp.prev != None):
            print(temp.data,"<->", end=" ")
            temp = temp.prev

        print(temp.data, "-> None")






dll = DoublyLinkedList()
dll.insertEnd(10)
dll.insertEnd(20)
dll.insertEnd(30)
dll.displayForward()
# dll.displayBackward()


dll.insertStart(100)
dll.insertStart(200)
dll.displayForward()
# dll.displayBackward()


dll.insertPosition(4, 400)
dll.displayForward()
# dll.displayBackward()


dll.deleteStart()
dll.displayForward()
# dll.displayBackward()


dll.deleteEnd()
dll.displayForward()

dll.deletePosition(3)
dll.displayForward()

dll.search(20)
dll.lengthofthelist()


dll.reverselist()
dll.displayForward()
dll.displayBackward()