class Linear_Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear =  -1



    def enqueue(self,data):
        if self.capacity == self.rear + 1:
            raise IndexError ("Queue is Full, so unable to add")
        
        if self.front == -1 and self.rear == -1 :
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            return

        self.rear = self.rear+1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            raise IndexError ("Queue is Empty, so unable to remove")

        if self.front == self.rear:
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            return value

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return value

    def peek(self):
        if self.front == -1 and self.rear == -1:
            raise IndexError("Queue is Empty, unable to view the values")

        return self.queue[self.front] 

    def is_empty(self):
        if self.front  == -1 and self.rear == -1:
            return True
        return False

    def is_full(self):
        return self.rear == self.capacity - 1

    def size(self):
        if self.front == -1:
            return 0

        return self.rear - self.front + 1

    def display(self):
        if self.front == -1:
            return []
        result = []
        current = self.front
        while current <= self.rear:
            result.append(self.queue[current])
            current += 1
        return result
    

        


List = Linear_Queue(4)

List.enqueue(20)

List.enqueue(30)
print(List.is_empty())
print(List.peek())
print(List.dequeue())
print(List.dequeue())

print(List.is_empty())



List.enqueue(20)
List.enqueue(30)
print(List.size())
List.enqueue(20)
print(List.is_full())

print(List.display())
        

