class Stack:
    stack = []
    def __init__(self,top=-1,m = 12):
        self.top = top
        self.m = m
    def push(self,value):
        if len(self.stack)<self.m:
            self.stack.append(self.value)
        else:
            isfull()
    def pop(self):
        if len(self.stack)>self.top:
            self.stack.pop()
        else:
            isEmpty()
    def isfull():
        print("Stack is Full")
    def isEmpty():
        print("Stack is Empty")
    def display(self):
        print(stack)
stack = Stack(-1,12)
stack.push(20)
stack.display()


            
