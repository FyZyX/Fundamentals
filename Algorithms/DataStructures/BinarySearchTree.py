class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.value == value:
            return False
        elif value < self.value:
            if self.left_child:
                return self.left_child.insert(value)
            else:
                self.left_child = Node(value)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(value)
            else:
                self.right_child = Node(value)
                return True

    def find(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left_child:
                return self.left_child.find(value)
            else:
                return False
        else:
            if self.right_child:
                return self.right_child.find(value)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()

    def inorder(self):
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.value))
            if self.right_child:
                self.right_child.inorder()

    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(str(self.value))


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

    def preorder(self):
        print('Preorder Traversal')
        self.root.preorder()

    def inorder(self):
        print('Ineorder Traversal')
        self.root.inorder()

    def postorder(self):
        print('Postorder Traversal')
        self.root.postorder()
