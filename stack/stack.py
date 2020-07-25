"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
   i.) added element must have index of last item in the array (len + 1 or [:-1])
   ii.) removed element must have index of last item in the array (len + 1 or [:-1])
   iii.) all indexes less than last item cannot be removed
   iv.)
   v.)
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self, size, storage):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage + int(value)

    def pop(self):
        self.storage[:-1]


stacky = Stack(16, [])
stacky.push(5)
print(stacky)
