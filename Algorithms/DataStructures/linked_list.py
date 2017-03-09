class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def next(self, next_node=None):
        if next_node is None:
            return self.next_node
        else:
            self.next_node = next_node


class LinkedList:
    def __init__(self, root_node=None):
        self.root = root_node
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, value):
        new_node = Node(value, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, value):
        current_node = self.root
        previous_node = None
        while current_node:
            if current_node.value == value:
                if previous_node:
                    previous_node.next(current_node.next())
                else:
                    self.root = current_node
                self.size -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.next()
        return False

    def find(self, value):
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return value
            else:
                current_node = current_node.next()
        return None
