class Node:
    def __init__(self,data):
        self.data = data
        self.below = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        new_node = Node(data)

        new_node.below = self.top
        self.top = new_node
        self.count += 1        
    
    def pop(self):
        if self.top is None:
            raise IndexError ("Connot pop from an empty stack")
        
        popped_node = self.top
        self.top = self.top.below
        self.count -= 1
        return popped_node.data
    
    def peek(self):
        if self.top is None:
            raise IndexError ("Stack is empty")
        return self.top.data
           
    
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False
        
    def size(self):
        return self.count
    
    def display(self):
        result = []
        current = self.top 
        
        while current is not None:
            result.append(current.data)
            current = current.below
        return result
    


box = Stack()

box.push(30)
box.push(20)
box.push(10)

# print(box.pop())

# print(box.peek())

# print(box.is_empty())

# print(box.size())

print(box.display())