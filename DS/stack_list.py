class StackList:
    def __init__(self, size):
        self.stack = []
        self.size = size
        
        
    def push(self, value):
        if(self.size == len(self.stack)):
            print(f"Stack overflow, cannot push the value {value}")
            
        else:
            self.stack.append(value)
            print(f"{value} pushed into the stack")
           
            
    def pop(self):
        if(self.isEmpty()):
            print("Stack underflow, there is no value to pop")
        
        else:
            removed = self.stack.pop()
            print(f"{removed} poped from the stack")
            
            
    def peek(self):
        if(self.isEmpty()):
            print("Stack underflow, there is no element in the stack")
        else:
            print("the peek value(top value) of the stack is ", self.stack[-1])
    
    
    def isEmpty(self):
        return len(self.stack) == 0
            
            
    def display(self):
        if(self.isEmpty()):
            print("Stack is empty")
        else:
            print("Stack:", self.stack)
        
        
        
sl = StackList(5)
sl.push(10)
sl.push(20)
sl.push(30)
sl.display()

sl.pop()
sl.display()

sl.peek()