class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleEndedQueueDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insertFront(self, data):
        newnode = Node(data)
        if(self.isEmpty()):
            self.head = newnode
            self.tail = self.head
            return
        
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode


    def deleteFront(self):
        if(self.isEmpty()):
            print("Deque is empty, no deleteFront operation")
            return
        
        if(self.head.next == None):
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next
        self.head.prev = None


    def insertRear(self, data):
        if(self.isEmpty()):
            self.insertFront(data)
            return
        
        newnode = Node(data)
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode


    def deleteRear(self):
        if(self.isEmpty()):
            print("Deque is empty, no deleteRear operation")
            return
        
        if(self.head.next == None):
            self.head = None
            self.tail = None
            return
        
        temp = self.tail.prev
        self.tail.prev = None
        temp.next = None
        self.tail = temp


    def isEmpty(self):
        return self.head == None
    

    def peekFront(self):
        if(self.isEmpty()):
            print("Deque is empty, no element in the queue")
            return
        
        print("Peek Front element:", self.head.data)

    
    def peekRear(self):
        if(self.isEmpty()):
            print("Deque is empty, no element in the queue")
            return
        
        print("Peek Rear element:", self.tail.data)


    def display(self):
        if(self.isEmpty()):
            print("Deque is empty")
            return
        
        temp = self.head
        print("Deque: ", end="")
        while (temp.next != None):
            print(temp.data, end=" ")
            temp = temp.next

        print(temp.data)








deqdl = DoubleEndedQueueDoublyLinkedList()
deqdl.insertFront(30)
deqdl.insertFront(20)
deqdl.insertFront(10)
deqdl.display()

deqdl.insertRear(100)
deqdl.insertRear(200)
deqdl.display()

deqdl.deleteFront()
deqdl.display()

deqdl.deleteRear()
deqdl.display()

deqdl.peekFront()

deqdl.peekRear()





