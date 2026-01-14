class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None


    def insertStart(self, data):
        newnode = Node(data)
        if(self.head == None):
            newnode.next = newnode
            newnode.prev = newnode
            self.head = newnode
            return
        
        lastnode = self.head.prev

        self.head.prev = newnode
        newnode.next = self.head
        newnode.prev = lastnode
        lastnode.next = newnode
        self.head = newnode


    def insertEnd(self, data):
        if(self.head == None):
            self.insertStart(data)
            return
        
        newnode = Node(data)
        lastnode = self.head.prev

        lastnode.next = newnode
        newnode.prev = lastnode
        newnode.next = self.head
        self.head.prev = newnode


    def insertPosition(self, index, data):
        if (index < 0):
            print("Invalid Index")
            return

        if(self.head == None):
            if(index == 0):
                self.insertStart(data)
            else:
                print("Index out of range")
            return
        
        if(index == 0):
            self.insertStart(data)
            return
        
        temp = self.head
        count = 0
        while (temp.next != self.head and count < index - 1):
            temp = temp.next
            count = count + 1

        if(temp.next == self.head and count == index - 1):
            newnode = Node(data)
            temp.next = newnode
            newnode.prev = temp
            newnode.next = self.head
            self.head.prev = newnode
            return
        
        if (count != index - 1):
            print("Index out of range")
            return
        
        newnode = Node(data)
        newnode.prev = temp
        newnode.next = temp.next
        temp.next = newnode
        newnode.next.prev = newnode
        

    def deleteStart(self):
        if(self.head == None):
            print("LinkedList is empty, no deletion")
            return
        
        if(self.head.next == self.head):
            self.head = None
            return
        
        prevnode = self.head.prev
        self.head = self.head.next
        self.head.prev = prevnode
        prevnode.next = self.head


    def deleteEnd(self):
        if(self.head == None):
            print("LinkedList is empty, no deletion")
            return
        
        if(self.head.next == self.head):
            self.head = None
            return
        
        lastnode = self.head.prev
        prev_lastnode = lastnode.prev
        prev_lastnode.next = self.head
        self.head.prev = prev_lastnode


            






    def displayForward(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        temp = self.head
        print("LinkedList(Forward): ", end="")
        while (temp.next != self.head):
            print(temp.data, "<=>", end=" ")
            temp = temp.next

        print(temp.data, "<=> (Head)")


    def displayBackward(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        temp = self.head.prev
        print("LinkedList(Backward):", end="")
        while (temp != self.head):
            print(temp.data, "<=>", end=" ")
            temp = temp.prev

        print(self.head.data, "<=> (Head)")

        

        








            
cdll = CircularDoublyLinkedList()
cdll.insertStart(10)
cdll.insertStart(20)
cdll.insertStart(30)
cdll.displayForward()
cdll.displayBackward()

cdll.insertEnd(40)
cdll.displayForward()

cdll.insertPosition(1, 100)
cdll.displayForward()

cdll.deleteStart()
cdll.displayForward()

cdll.deleteEnd()
cdll.displayForward()



