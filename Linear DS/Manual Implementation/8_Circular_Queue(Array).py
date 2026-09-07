class Circular_Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, value):
        if self.count == self.capacity:
            raise IndexError("Array is full")

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.count +=1

    def dequeue(self,):
        if self.count == 0:
            raise IndexError ("Cannot access array to 0 if we hit the end")

        value = self.queue[self.front]

        self.front = (self.front + 1)% self.capacity
        self.count -=1
        return value

    def peek(self):
        if self.count == 0:
            raise IndexError("Cannot access array to 0 if we hit the end")
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def size(self):
        return self.count 
            

    def display(self):
        if self.count == 0:
            raise IndexError("Cannot access array to 0 if we hit the end")
        result = []
    
        current = self.front
        for _ in range(self.count):
            result.append(self.queue[current])
            current = (current + 1) % self.capacity
        return result


List = Circular_Queue(6)

List.enqueue(10)
List.enqueue(20)
List.enqueue(30)
List.enqueue(40)

print(List.display())

List.dequeue()
List.dequeue()

print(List.display())

List.enqueue(10)
List.enqueue(10)
List.enqueue(40)
List.enqueue(40)
print(List.display())

print(List.peek())

print(List.is_empty())

print(List.is_full())

print(List.size())