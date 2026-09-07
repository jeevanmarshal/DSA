import ctypes
class MyArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.array = self._make_array(self.capacity) 
    
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def access(self, index):
        if not (0 <= index < self.count):
            raise IndexError ("Index out of bounds")
        return self.array[index]
    
    def update(self, index, value):
        if not (0 <= index < self.count):
            raise IndexError("Index out of boounds")
        self.array[index] = value

    def append(self, value):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.count] = value
        self.count += 1

    def insert(self, index, value):
        if not (0 <= index <= self.count):
            raise IndexError("Index out of boounds")
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        
        for i in range(self.count, index-1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.count +=1

    def delete(self, index):
        if not (0 <= index < self.count):
            raise IndexError("Index out of boounds")
        
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.count -=1
    
    def resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.count
        self.array = new_array
        self.capacity = new_capacity

    def display(self):
        print("[",end='')

        for i in range(self.count):
            print(self.array[i], end='')

            if i != self.count -1 :
                print(', ', end='')
        print(']')


    def search(self, value):
        for i in range(self.count):
            if self.array[i] == value:
                return i
        return 'Not Found'
        
    def reverse(self):
        left = 0
        right = self.count - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left +=1
            right -=1

    def traverse(self):
        result = []
        for i in range(self.count):
            result.append(self.array[i])
        return result
    
    def is_empty(self):
        return self.count == 0



arr = MyArray(5)

arr.append(78)
arr.append(32)

arr.append(34)

print(arr.display())

print(arr.search(34))

arr.reverse()

print(arr.display())           


print(arr.traverse())

print(arr.is_empty())