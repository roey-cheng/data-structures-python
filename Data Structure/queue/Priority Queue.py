class PriorityQueue:

    def __init__(self):
        self.binary_heap = [0]
        self.size = 0

    def percolate_up(self, index):
        while index // 2 > 0 and self.binary_heap[index] < self.binary_heap[index // 2]:
            self.binary_heap[index], self.binary_heap[index // 2] = self.binary_heap[index // 2], self.binary_heap[index]
            index = index // 2
    
    def insert(self, value):
        self.binary_heap.append(value)
        self.size += 1
        self.percolate_up(self.size)

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def percolate_down(self, index):
        while (index * 2) <= self.size:
            smallest = self.get_smaller_child_index(index)
            if self.binary_heap[index] > self.binary_heap[smallest]:
                self.binary_heap[index], self.binary_heap[smallest] = self.binary_heap[smallest], self.binary_heap[index]
            index = smallest

    def get_smaller_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.binary_heap[index * 2] < self.binary_heap[index * 2 + 1]:
                return index * 2 + 1
            else:
                return index * 2

    def delete_minimum(self):
        root_i = 1
        minimum_v = self.binary_heap[root_i]
        self.binary_heap[root_i] = self.binary_heap[self.size]
        self.binary_heap.pop()
