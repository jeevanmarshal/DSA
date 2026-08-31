class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node 


    def traverse_forward(self):
        result =[]
        current = self.head
        while current is not None:
            result.append(current.data) 
            current = current.next
        return result


    def traverse_backward(self):
        result = []
        current = self.tail
        while current is not None:
           result.append(current.data)
           current = current.prev
        return result
    
    def delete_head(self):
        if self.head is None:
            raise IndexError ("Cannot delete from empty list")
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
    
    def delete_tail(self):
        if self.tail is None:
            raise IndexError ("Cannot delete from empty list")
        self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

    def delete_by_value(self, value):
        if self.head is None:
            return -1
        
        current = self.head
        while current is not None:
            if current.data == value:
                if current == self.head:
                    self.delete_head()
                    return
                if current == self.tail:
                    self.delete_tail()
                    return
                
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            
            current = current.next
        return -1
    
    def insert_after_value(self, target_value, new_value):
        current = self.head
        add = new_value
        new_node = Node(new_value)
        while current is not None:
            if current.data == target_value:
                if current == self.tail:
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                    return
                
                new_node.prev = current 
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                return
            
            current = current.next
        return -1



List = DoublyLinkedList()

List.insert_at_head(30)
List.insert_at_head(32)
List.insert_at_head(36)

List.insert_at_tail(23)

print(List.traverse_forward())

List.delete_tail()

print(List.traverse_backward())

List.delete_by_value(32)

print(List.traverse_forward())

List.insert_after_value(36,56)
print(List.traverse_forward())