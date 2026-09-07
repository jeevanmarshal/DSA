class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linear_Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.count += 1
            return

        self.rear.next = new_node
        self.rear = new_node
        self.count += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError ("There is no Node to remove")
        value = self.front.data
        if self.front is self.rear:
            self.front = None
            self.rear = None
            self.count -=1
            return value

        self.front = self.front.next
        self.count -= 1
        return value

    def peek(self):
        if self.front is None:
            raise IndexError("There is no node view")

        return self.front.data

    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self.count 

    def display(self):
        if self.front is None:
            return []
        result = []

        current = self.front
        for _ in range(self.count):
            result.append(current.data)
            current = current.next
        return result

List = Linear_Queue()

List.enqueue(10)
List.enqueue(20)
print(List.dequeue())
List.enqueue(30)
List.enqueue(40)

print(List.peek())
print(List.is_empty())
print(List.size())
print(List.display())
