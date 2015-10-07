class Node(object):

    def __init__(self, data=None):          # Initalizes a node without pointer
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
        head_str = 'head: ' + str(self.head) if self.head else ''
        tail_str = 'tail: ' + str(self.tail) if self.tail else ''
        return 'LinkedList({}{})'.format(head_str, tail_str)

    def is_empty(self):  # returns true if list is empty
        return self.size == 0

    def is_valid(self):
        head_valid = self.head is not None
        tail_valid = self.tail is not None
        size_valid = self.size > 0
        # sets aboves to boolean values
        if head_valid and tail_valid and size_valid:
            return True
        elif not head_valid and not tail_valid and not size_valid:
            return True
        else:
            return False

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        if self.tail is None:
            self.tail = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None:
            raise ValueError('List is empty')
        self.head = self.head.next
        self.size -= 1

    def calculate_size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count


class HashTable():

    def __init__(self, table_size=10):
        self.table = []
        self.table_size = table_size
        self.item_count = 0
        for bucket in range(table_size):
            self.table.append(LinkedList())

    def load_factor(self):
        load = self.item_count / self.table_size
        return load

    def get_bucket(self, key):
        bucket_id = hash(key) % self.table_size
        correct_bucket = self.table[bucket_id]
        return correct_bucket

    def set(self, key, value):
        correct_bucket = self.get_bucket(key)
        correct_bucket.insert_at_head((key, value))
        self.item_count += 1

    def get(self, key):
        correct_bucket = self.get_bucket(key)
        current_node = correct_bucket.head
        while current_node.data is not None:
            if key in current_node.data:
                return current_node.data
            else:
                current_node = current_node.next_node
        return KeyError("This key is not in this list!")

    def update(self, key, new_value):
        correct_bucket = self.get_bucket(key)
        current_node = correct_bucket.head
        found = False
        while not found and current_node.data is not None:
            if key in current_node.data:
                found = True
                current_node.data = (key, new_value)
                return '{} updated to {}'.format(key, new_value)
            else:
                current_node = current_node.next_node
        return KeyError('Cannot update: key not in list!')
