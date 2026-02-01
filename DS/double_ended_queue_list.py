class DoubleEndedQueueList:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = -1


    def insertFront(self, value):
        if(self.isFull()):
            print("Deque is full, no insertFront operation")
            return
        
        if(self.isEmpty()):
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size

        self.deque[self.front] = value
        print(f"{value} is inserted at front of the queue")


    def deleteFront(self):
        if(self.isEmpty()):
            print("Deque is empty, no deleteFront operation")
            return
        
        removed = self.deque[self.front]
        if(self.front == self.rear):
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"{removed} is deleted from the front of the queue")


    def insertRear(self, value):
        if(self.isFull()):
            print("Deque is full, no insertRear operation")
            return
        
        if(self.isEmpty()):
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        
        self.deque[self.rear] = value
        print(f"{value} is inserted at rear of the queue")


    def deleteRear(self):
        if(self.isEmpty()):
            print("Deque is empty, no deleteRear operation")
            return
        
        removed = self.deque[self.rear]
        if(self.front == self.rear):
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        
        print(f"{removed} is deleted from rear of the queue")


    def peekFront(self):
        if(self.isEmpty()):
            print("Deque is empty, no element in the list")
            return
        print("Peek Front element:", self.deque[self.front])


    def peekRear(self):
        if(self.isEmpty()):
            print("Deque is empty, no element in the list")
            return
        print("Peek Rear element:", self.deque[self.rear])


    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)
        

    def isEmpty(self):
        return self.front == -1
    

    def display(self):
        if(self.isEmpty()):
            print("Deque is empty")
            return
        
        i = self.front
        print("Deque: ", end="")
        while True:
            print(self.deque[i], end=" ")

            if(i == self.rear):
                break
            i = (i + 1) % self.size
        print()





deql = DoubleEndedQueueList(5)
deql.insertFront(30)
deql.insertFront(20)
deql.insertFront(10)
deql.display()

deql.deleteFront()
deql.display()

deql.insertRear(50)
deql.insertRear(60)
deql.insertRear(70)
deql.display()

deql.deleteRear()
deql.display()

deql.peekFront()

deql.peekRear()
