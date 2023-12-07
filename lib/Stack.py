class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit 

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack Full")

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for index, item in enumerate(reversed(self.items), start=0):
            if item == target:
             return index
        return -1
