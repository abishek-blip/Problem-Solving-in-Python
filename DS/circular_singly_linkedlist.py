class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None


    def insertStart(self, data):
        newnode = Node(data)
        if (self.head == None):
            self.head = newnode
            newnode.next = newnode
            return
        
        temp = self.head

        while (temp.next != self.head):
            temp = temp.next

        newnode.next = self.head
        temp.next = newnode
        self.head = newnode


    def insertEnd(self, data):
        newnode = Node(data)
        if(self.head == None):
            self.head = newnode
            newnode.next = newnode
            return
        
        temp = self.head
        while (temp.next != self.head):
            temp = temp.next

        temp.next = newnode
        newnode.next = self.head


    def insertPosition(self, index, data):
        if (index < 0):
            print("Invalid Index")
            return
    
        if (self.head == None):
            if(index == 0):
                self.insertStart(data)
            else:
                print("LinkedList is empty and invalid index")
            return
        
        if (index == 0):
            self.insertStart(data)
            return
        
        newnode = Node(data)
        temp = self.head
        count = 0
        while (temp.next != self.head and count < index - 1):
            count = count + 1
            temp = temp.next
        
        if (count != index - 1):
            print("Index out of range")
            return
        
        newnode.next = temp.next
        temp.next = newnode


    def deleteStart(self):
        if(self.head == None):
            print("LinkedList is empty, no deletion")
            return
        if(self.head.next == self.head):
            self.head = None
            return
        
        temp = self.head
        while (temp.next != self.head):
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    
    def deleteEnd(self):
        if(self.head == None):
            print("LinkedList is empty, no deletion")
            return
        if(self.head.next == self.head):
            self.head = None
            return
        
        temp = self.head
        while (temp.next.next != self.head):
            temp = temp.next

        temp.next = self.head


    def deletePosition(self, index):
        if(index < 0):
            print("Invalid Index")
            return

        if(self.head == None):
            print("LinkedList is empty, no deletion")
            return
        
        if(index == 0):
            self.deleteStart()
            return
        
        temp = self.head
        count = 0
        while (temp.next != self.head and count < index - 1):
            temp = temp.next
            count = count + 1

        if(temp.next == self.head):
            print("Index out of range")
            return
        
        temp.next = temp.next.next

        
    def search(self, data):
        if(self.head == None):
            print("LinkedList is empty, no search operation")
            return
        
        temp = self.head
        count = 0
        while True:
            if(temp.data == data):
                print("the value", data, "is found at the index", count)
                return
            
            temp = temp.next
            count = count + 1

            if(temp == self.head):
                break

        print("the value", data, "is not found at any index")


    def lengthofthelist(self):
        if(self.head == None):
            print("LinkedList is empty the length of the list is zero")
            return
        
        count = 1
        temp = self.head.next
        while (temp != self.head):
            count = count + 1
            temp = temp.next

        print("Total length of the list is", count)


    def reverselist(self):
        if(self.head == None):
            print("LinkedList is empty, no reverse operation")
            return
        
        if(self.head.next == self.head):
            print("LinkedList has only one node, no reverse needed")
            return
        
        prev = self.head
        temp = self.head.next
        while (temp != self.head):
            nextnode = temp.next
            temp.next = prev
            prev = temp
            temp = nextnode

        self.head.next = prev
        self.head = prev





    def display(self):
        if (self.head == None):
            print("LinkedList is empty")
            return
        
        temp = self.head
        print("LinkedList:", end=" ")
        while (temp.next != self.head):
            print(temp.data, "=>",end=" ")
            temp = temp.next

        print(temp.data, "=> (Head)")






csll = CircularSinglyLinkedList()
csll.insertStart(10)
csll.insertStart(20)
csll.insertStart(30)
csll.display()

csll.insertEnd(40)
csll.insertEnd(50)
csll.display()

csll.insertPosition(2, 60)
csll.display()

csll.deleteStart()
csll.display()

csll.deleteEnd()
csll.display()

csll.deletePosition(1)
csll.display()

csll.search(40)

csll.lengthofthelist()

csll.reverselist()
csll.display()

csll.reverselist()
csll.display()