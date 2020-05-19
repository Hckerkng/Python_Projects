class Queue:
    queue = [""]
    rear = 0
    front = 0
    def __init__(self,m):
        self.m = m
        self.queue = self.queue*m
        self.rear = self.rear
        self.front = self.front 
    def is_full():
        return "Queue is Full"
    def is_Empty():
        return "Queue is Empty"
    def enqueue(self,value):
        if self.rear < self.m:
            self.queue[self.rear] = value
            self.rear+=1
            return f"Queue is:-{self.queue[self.front:self.rear]}"
        else:
            return Queue.is_full()
    def dequeue(self):
        if self.rear > 0:
            self.queue=self.queue[self.front+1:]
            self.queue+=[""]
            self.rear-=1
            return f"Queue is:-{self.queue[self.front:self.rear]}"
        else:
            return Queue.is_Empty()
    def display(self):
        return f"Your Queue is:-{self.queue[self.front:self.rear]}"
    def __str__(self):
        return f"Queue is:-{self.queue[self.front:self.rear]}"
    def __repr__(self):
        return f"Queue is:-{self.queue[self.front:self.rear]}"
