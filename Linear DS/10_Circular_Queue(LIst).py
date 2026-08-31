class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Circular_Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            new_node.next = new_node
            self.front = new_node
            self.rear = new_node
            self.count += 1
            return 

        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.count += 1
        return

    def dequeue(self):
        if self.front is None:
            raise IndexError("There is no nodes to remove")
        value = self.front.data
        if self.front is self.rear:
            self.front = None
            self.rear = None
            self.count -= 1
            return value

        self.rear.next = self.front.next
        self.front = self.front.next
        self.count -=1
        return value

    def display(self):
        if self.front is None:
            return []
        result = []

        current = self.front
        for _ in range(self.count):
            result.append(current.data)
            current = current.next
        return result

List = Circular_Queue()

List.enqueue(40)
List.enqueue(30)
List.enqueue(20)
List.enqueue(10)

print(List.dequeue())

print(List.display())

print(List.dequeue())
