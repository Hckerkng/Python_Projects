class Queue:
    def __init__(self,data = []):
        self.data = data
    def insert(self,value):
        self.data.insert(value)
    def delete(self):
        self.data.remove(0)

