class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def insertStart(self, data):
        newnode = Node(data)
        if(self.head == None):
            self.head = newnode
            return
        
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
        
        newnode = Node(data)
        count = 0
        temp = self.head
        while ((temp != None) and (count < index)):
            temp = temp.next
            count = count + 1

        if(temp == None):
            print("Index out of range")
            return
        
        newnode.next = temp.next
        temp.next = newnode


    def deleteStart(self):
        if(self.head == None):
            print("LinkedList is empty no operation is done for deleteStart()")
            return

        temp = self.head.next
        self.head = temp  


    def deleteEnd(self):
        if(self.head == None):
            print("Linkedlist is empty no operation is done for deleteEnd()")
            return
        
        temp = self.head
        while temp.next.next != None:
            temp = temp.next

        temp.next = None

        
    def deletePosition(self, index):
        if(index < 0):
            print("Invalid Index")
            return
        
        if(index == 0):
            self.deleteStart()
            return
        
        temp = self.head
        count = 0

        while ((temp.next != None) and (count < index - 1)):
            temp = temp.next
            count = count + 1

        if(temp.next == None):
            print("Index out of range")
            return

        temp.next = temp.next.next
        

    def search(self, data):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        count = 0
        isfound = False
        temp = self.head

        while (temp != None):
            if(temp.data == data):
                print("the value", data, "is found at the index ", count)
                isfound = True
                break

            temp = temp.next
            count = count + 1

        if(isfound == False):
            print("the value", data, " is not found at any index")


    def lengthofthelist(self):
        if(self.head == None):
            print("LinkedList is empty the length of the list is zero")
            return
        
        count = 0
        temp = self.head
        while (temp != None):
            count += 1
            temp = temp.next

        print("Total length of the list is", count)


    def reverselist(self):
        if(self.head == None):
            print("LinkedList is empty no reverse operation is performed")
            return
        
        prev = None
        curr = self.head
        while curr != None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        self.head = prev
        

    def display(self):
        if(self.head == None):
            print("LinkedList is empty")
            return
        
        temp = self.head
        print("LinkedList: ",end="")

        while temp.next != None:
            print(temp.data,"=> ", end="")
            temp = temp.next
        
        print(temp.data,"=> None")
    




sll = SinglyLinkedList()
sll.insertEnd(10)
sll.insertEnd(20)
sll.insertEnd(30)
sll.display()

sll.insertStart(100)
sll.insertStart(200)
sll.display()

sll.insertPosition(0, 300)
sll.insertPosition(1, 400)
sll.insertPosition(7, 500)
sll.insertPosition(6, 600)
sll.display()

sll.deleteStart()
sll.deleteStart()
sll.display()

sll.deleteEnd()
sll.deleteEnd()
sll.display()

sll.deletePosition(3)
sll.display()

sll.search(10)
sll.search(0)
sll.search(400)
sll.display()

sll.lengthofthelist()

sll.reverselist()
sll.display()
