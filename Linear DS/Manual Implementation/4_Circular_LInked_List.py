class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
    
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node
    
    def search(self, value):
        if self.head is None:
            return -1
        current = self.head
        index = 0

        while True:
            if current.data == value:
                return index
            current = current.next
            index +=1

            if current == self.head:
                break
        return -1
               
    def traverse(self):
        result = []
        if self.head is None:
            return []
   
        current = self.head

        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result
    
    def delete_head(self):
        if self.head is None:
            return -1
        
        current = self.head 
        while True:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            
            self.head = self.head.next
            self.tail.next = self.head
            return

    def delete_tail(self):
        if self.head is None:
            return -1

        current = self.head

        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return 
            
        while current.next != self.tail:
            current = current.next

        current.next = self.head
        self.tail = current    

    def delete_by_value(self, value):
        if self.head is None:
            return 
        
        if self.head == value:
            self.delete_head()
            return
        
        if self.tail == value:
            self.delete_tail()
            return

        current = self.head

        while current.next != self.head:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        return -1

List = Circular_Linked_List()


List.insert_at_head(40)
List.insert_at_head(30)
List.insert_at_head(20)
List.insert_at_head(10)

print(List.traverse())


print(List.search(30))

# List.delete_head()
# List.delete_tail()

List.delete_by_value(30)
print(List.traverse())