class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = [None]*capacity
        self.count = 0

    def _hash(self, key):
        total = 0
        for char in key:
            total = total + ord(char)
        return total % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        current = self.hash[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return 
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.hash[index]
        self.hash[index] = new_node
        self.count += 1

    def search(self, key):
        index = self._hash(key)
        current = self.hash[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash(key)

        current = self.hash[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.hash[index] = current.next
                else:
                    previous.next = current.next
                self.count -= 1
                return
            previous = current
            current = current.next 

        raise KeyError (f'Key is not found: {key}')


    def display(self):
        for index in range(self.capacity):
            current = self.hash[index]

            if current is None:
                print(f"Bucket {index} : Empty")
                continue
    
            result = []

            while current is not None:
                result.append(f"({current.key} : {current.value})")
                current = current.next

            print(f'Bucket {index} : {" -> ".join(result)}')

    def size(self):
        return self.count


    def is_empty(self):
        return self.count == 0

    def update(self,key, value):
        index = self._hash(key)
        current = self.hash[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
            
        raise KeyError(f"Key not found: {key}")
                

    

list = HashMap(8)


list.insert('CAT', 100)
list.insert('DOG', 200)


print(list.search('DOG'))

list.delete('CAT')

list.insert('PAT',10)
list.insert('TAT',10)
print(list.display())


print(list.size())


print(list.is_empty())

print(list.update('CAT',500))



