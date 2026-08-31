class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Circular_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        
        new_node.next = self.head
        new_node.prev = self.tail

        self.head.prev = new_node
        self.tail.next = new_node

        self.head = new_node
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            new_node.next = new_node
            new_node.prev = new_node
            return
        
        new_node.next = self.head 
        new_node.prev = self.tail

        self.tail.next = new_node
        self.head.prev = new_node

        self.tail = new_node
        
    def traverse_forward(self):
        result = []

        if self.head is None:
            return result
        
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result
    
    def traverse_backward(self):
        result = []
        if self.tail is None:
            return result
        
        current = self.tail
        while True:
            result.append(current.data)
            current = current.prev
            if current == self.tail:
                break
        return result
    
    def insert_after_value(self, value, data):
        new_node = Node(data)

        if self.head is None:
            return -1
        
        current = self.head

        while True:
            if current.data == value:
                next_node = current.next
                current.next = new_node
                new_node.prev = current

                new_node.next = next_node
                next_node.prev = new_node
                return
            current = current.next

            if current == self.head:
                break
        return -1
    
    def insert_before_value(self, value, data):
        new_node = Node(data)

        if self.head is None:
            return -1
        
        current = self.head

        while True:
            if current.data == value:
                prev_node = current.prev
                current.prev = new_node
                new_node.next = current  

                new_node.prev = prev_node
                prev_node.next = new_node
                return
            current = current.next
            if current == self.head:
                break
        return -1
    
    def delete_by_value(self, value):
        if self.head is None:
            return -1
        
        current = self.head

        while True:
            if current.data == value:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                    return
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                    return
                else:
                    next_node = current.next
                    prev_node = current.prev
                    next_node.prev = prev_node
                    prev_node.next = current.next
                    return
               
            current = current.next
            if current == self.head:
                break
        return -1
    
    def delete_head(self):
        if self.head is None:
            return -1
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        current = self.head
        self.head = current.next
        self.head.prev = self.tail
        self.tail.next = self.head

        return
    
    def delete_tail(self):
        if self.head is None:
            return -1
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.prev

        self.tail.next = self.head
        self.head.prev = self.tail
        return


List = Doubly_Circular_Linked_list()

List.insert_at_head(40)
List.insert_at_head(30)
List.insert_at_head(20)
List.insert_at_head(10)
List.insert_at_tail(50)
List.insert_after_value(30, 35)
List.insert_before_value(30, 25)
print(List.traverse_forward())

List.delete_by_value(10)
List.delete_head()
List.delete_tail()
print(List.traverse_forward())


