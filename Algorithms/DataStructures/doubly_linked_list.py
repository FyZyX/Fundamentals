class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def next(self, next_node=None):
        if next_node is None:
            return self.next_node
        else:
            self.next_node = next_node

    def prev(self, prev_node=None):
        if prev_node is None:
            return self.prev_node
        else:
            self.prev_node = prev_node


class LinkedList:
    def __init__(self, root_node=None):
        self.root = root_node
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, value):
        new_node = Node(value, self.root)
        if self.root:
            self.root.prev(new_node)
        self.root = new_node
        self.size += 1

    def remove(self, value):
        current_node = self.root
        while current_node:
            if current_node.value == value:
                next_node = current_node.next()
                previous_node = current_node.prev()

                if next_node:
                    next_node.prev(previous_node)
                if previous_node:
                    previous_node.next(next_node)
                else:
                    self.root = current_node
                self.size -= 1
                return True
            else:
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
