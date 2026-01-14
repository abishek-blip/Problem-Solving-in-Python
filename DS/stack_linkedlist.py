class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class StackLinkedList:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.top = None
        
        
    def push(self, value):
        if(self.size == self.count):
            print("Stack Overflow")
            return
        
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode
        self.count = self.count + 1
        print(f"{value} is pushed to the stack")
        
        
    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow, no pop operation")
            return
        
        popped = self.top.value
        self.top = self.top.next
        self.count = self.count - 1
        print(f"{popped} is popped from the stack")
        
        
    def peek(self):
        if(self.isEmpty()):
            print("Stack Underflow")
        else:
            print(f"Peek Element:{self.top.value}")

 
    def isEmpty(self):
        return self.count == 0
        
        
    def display(self):
        if(self.isEmpty()):
            print("Stack Underflow")
            return
        
        temp = self.top
        print("Stack(Top -> Bottom):", end=" ")
        while (temp.next != None):
            print(temp.value, " => ", end= "")
            temp = temp.next
        
        print(temp.value, " => None(End of Stack)")    
     
            
            
sll = StackLinkedList(5)
sll.push(10)
sll.push(20)
sll.push(30)
sll.display()
            
sll.pop()
sll.display()
            
sll.peek()         
sll.display()