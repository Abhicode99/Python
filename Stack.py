

class Stack:
    def __init__(self):
        self.items=[2,3.5]
        print('This step executed')

    def is_empty(self):
        return not self.items

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str(self):
        return str(self.items)



