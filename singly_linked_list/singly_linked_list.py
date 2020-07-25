class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        #  the reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_text


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        # create a node - whos next_node is pointing to the current head node value
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:  # if self.head is none and self.tail is none
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
