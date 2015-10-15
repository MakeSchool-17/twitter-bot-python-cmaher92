# [brian] In python it's looks a little weird to have the filename start with a
# capital letter. This file should probably be called `hashtable`, and that
# way other modules can call `import hashtable` instead of `import Hashtable`.
# It's not a big difference, the worst breaking convention will do is get you
# some dirty looks, but following convention makes your code more readable and
# easier to understand.

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

        # [brian] You could also write the above as:
        return 'LinkedList(head: {} tail: {})'.format(self.head or '', self.tail or '')

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

        # [brian] Python has a pretty fun definition of "true" and "false",
        # you can use more than just booleans when writing your if statements.
        # the below also works:
        if self.head and self.tail and self.size:
            return True
        elif self.head and not self.tail and not self.size:
            return True
        return False
        # here's a link with more about the rules:
        # https://www.udacity.com/wiki/cs258/truthiness-in-python

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
    # [brian] This looks great! This whole file is very neat and clean

    def __init__(self, table_size=10):
        self.table = []
        self.table_size = table_size
        self.item_count = 0
        for bucket in range(table_size):
            self.table.append(LinkedList())

        # [brian] You could also write this:
        # (it's convention to use `_` for variables you aren't going to use)
        self.table = [LinkedList() for _ in range(table_size)]

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
        # [brian] There are times when you want to return exceptions,
        # but I don't think this is one of them. If a user were to wrap
        # a call to this method in a try-catch block the `catch`
        # would never be triggered. Instead you should:
        raise KeyError("This key is not in this list!")

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
