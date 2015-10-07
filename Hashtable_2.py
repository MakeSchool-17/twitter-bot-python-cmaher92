class Node(object):
    def __init__(self, data=None):          # Initalizes a node without pointer or data
        self.data = data
        self.next = None

    def __str__(self):
        has_next = ', has next' if self.next else 'no next '
        return 'Node({}{})'.format(self.data, has_next)

class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self):
        head_str = "head: " + str(self.head)
