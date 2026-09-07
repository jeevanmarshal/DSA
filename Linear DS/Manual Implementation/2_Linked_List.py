class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single_Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
            
    def search(self, value):
        current = self.head
        position = 0
        while current is not None:
            if current.data == value:
                return position
    
            current = current.next
            position += 1
        return -1
    
    def traverse(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.data)
            current = current.next
        return result
    
    def delete_head(self):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        self.head = self.head.next
        
    def delete_by_value(self, value):
        if self.head is None:
            return -1
        
        if self.head.data == value:
            self.head = self.head.next
            return
    
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return current
            current = current.next
        return -1
    
    def size(self):
        current = self.head
        size = 0

        while current is not None:
            current = current.next
            size +=1
        return size
    
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

       
         


List = Single_Linked_List()

List.insert_at_head(20)
List.insert_at_head(25)
List.insert_at_head(30)
print(List.search(20))
List.insert_at_tail(15)
print(List.traverse())
List.delete_head()
List.delete_by_value(25)
print(List.traverse())
print(List.size())

List.reverse()
print(List.traverse())