class QueueList:
    def __init__(self, size):
        self.queue = []
        self.size = size


    def enqueue(self, value):
        if(self.isFull()):
            print("Queue is full, no enqueue operation")
            return

        self.queue.append(value)
        print(f"{value} enqueued in the queue")


    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty, no dequeue operation")
            return
        
        removed = self.queue.pop(0)
        print(f"{removed} dequeued from the queue")


    def peek(self):
        if(self.isEmpty()):
            print("Queue is empty, no element present")
            return
        
        print("Peek element:", self.queue[0])


    def isEmpty(self):
        return len(self.queue) == 0
    

    def isFull(self):
        return len(self.queue) == self.size


    def display(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return
        
        print("Queue (Front -> Rear): ", self.queue)

        

ql = QueueList(7)
ql.enqueue(10)
ql.enqueue(20)
ql.enqueue(30)
ql.display()

ql.dequeue()
ql.display()

ql.peek()
ql.display()


