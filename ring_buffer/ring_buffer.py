class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None]*capacity
        # capacity == 5
        self.capacity = capacity
        # for indexes
        self.current = 0


# adds the given element to the buffer
# should not return any None

    def append(self, item):
        # appending to the list
        self.storage[self.current] = item
        # iterating through the current index
        self.current += 1
        self.current = self.current % self.capacity


# returns all of the elements in the buffer in a list in their given order
# should not return None


    def get(self):
        # return self.storage[:self.current]
        arr = []
        for element in self.storage:
            if element is not None:
                # append the result to arr
                arr.append(element)
        # return array
        return arr
