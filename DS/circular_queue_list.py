class CircularQueueList:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1


    def enqueue(self, value):
        if(self.isFull()):
            print("Circular Queue is full, no enqueue operation")
            return
        
        if(self.isEmpty()):
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"{value} enqueued in the queue")


    def dequeue(self):
        if(self.isEmpty()):
            print("Circular Queue is empty, no dequeue operation")
            return
        
        removed = self.queue[self.front]

        if(self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"{removed} dequeued from the queue")


    def peek(self):
        if(self.isEmpty()):
            print("Circular Queue is empty, no element present in the Queue")
            return
        
        print("Peek element:", self.queue[self.front])


    def isEmpty(self):
        return self.front == -1
    

    def isFull(self):
        return ((self.front) == (self.rear + 1) % self.size)
    

    def display(self):
        if(self.isEmpty()):
            print("Circular Queue is empty")
            return
        
        print("Circular Queue: ", end="")
        index = self.front

        while True:
            print(self.queue[index], end="  ")

            if (index == self.rear):
                break

            index = (index + 1) % self.size

        print()




cql = CircularQueueList(5)
cql.enqueue(10)
cql.enqueue(20)
cql.enqueue(30)
cql.display()

cql.dequeue()
cql.display()

cql.peek()
cql.display()
