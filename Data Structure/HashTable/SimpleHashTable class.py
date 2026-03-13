class SimpleHashTable:
    def __init__(self, size = 7):
        self.size = size
        self.slots = [None] * 7

    def __str__(self):
        return str(self.slots)
    
    def get_hash_index(self, key, step = 0):
        return (key + step) % self.slots
    
    def push(self, key):
        index = self.get_hash_index(key)
        self.slots[index] = key 

    def __len__(self):
        count = 0
        for element in self.slots:
            if element is not None:
                count += 1
        return count
    
    def get_load_factor(self):
        return self.__len__() / self.size