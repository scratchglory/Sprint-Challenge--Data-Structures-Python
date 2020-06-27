class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        # creates a node to add
        node = Node(value)

        # checks if this is empty
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        # traverse through all nodes until we see the value or can't go further
        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # print("NODE", node)  # object
        # print("PREV", prev)  # None

        # set current node
        current = self.head
        while current is not None:
            # instantiate getting the next node
            next_node = current.get_next()
            # set the current with the previous node
            current.set_next(prev)
            # previous is current
            prev = current
            # current is the next node that was fetched
            current = next_node
        # the head is now the previous
        self.head = prev
