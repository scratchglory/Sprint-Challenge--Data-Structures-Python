class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            # checking left
            if self.left:
                self.left.insert(value)
            else:
                self.left = Tree(value)
        else:
            # checking right
            if self.right:
                self.right.insert(value)
            else:
                self.right = Tree(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                # if left exist, recurisve find
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                # if right exists, recursive find
                return self.right.contains(target)
            else:
                return False
