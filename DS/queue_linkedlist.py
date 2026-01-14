class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        newnode = Node(value)
        
        if(self.isEmpty()):
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

        print(f"{value} is enqueued in the queue")


    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is empty, no dequeue operation")
            return
        
        removed = self.front.value
        if(self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

        print(f"{removed} is dequeued from the queue")


    def peek(self):
        if(self.isEmpty()):
            print("Queue is empty, no element present in the queue")
            return
        
        print("Peek element:", self.front.value)


    def count(self):
        if(self.isEmpty()):
            print("Queue is empty, count is zero")
            return
        
        count = 0
        temp = self.front
        while(temp != None):
            count += 1
            temp = temp.next
            
        print("Count:", count)
        

    def isEmpty(self):
        return self.front == None


    def display(self):
        if(self.isEmpty()):
            print("Queue is empty")
            return
        
        temp = self.front
        print("Queue (Front -> Rear):", end=" ")
        while (temp.next != None):
            print(temp.value, end=" => ")
            temp = temp.next

        print(temp.value, "=> None")




qll = QueueLinkedList()
qll.enqueue(10)
qll.enqueue(20)
qll.enqueue(30)
qll.enqueue(40)
qll.display()

qll.dequeue()
qll.display()

qll.peek()

qll.count()
