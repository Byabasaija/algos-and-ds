class MyList:
    def __init__(self):
        self.data = [None, None, None, None]
        self.size = 0
        self.capacity = 4

    def __resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity
        

    def append(self, value):
        if self.size >= self.capacity:
            self.__resize()
           
        self.data[self.size] = value
        self.size += 1

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]
    
    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def __len__(self):
        return self.size

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size >= self.capacity:
            self.__resize()
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        self.data[index] = value
        self.size += 1
        

           
        



my_list = MyList()
my_list.append("hello")
my_list.append("world")
my_list.append(42)
my_list.append(3.14)
my_list.append("Python")
print(f"Size: {my_list.size}")
print(f"Capacity: {my_list.capacity}")
print(f"Data: {my_list.data}")
print(my_list[0])  # Should print "hello"
print(my_list[1])  # Should print "world"
print(my_list[7])  # Should raise IndexError

