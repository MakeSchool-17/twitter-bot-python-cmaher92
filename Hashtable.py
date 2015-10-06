class Hashtable:

    def __init__(self):
        self.hashtable = []  # creates the list type for the table
        while len(self.hashtable) < 10:
            self.hashtable.append(LinkedList())  # adds linked lists to hashtable
        self.size = 0
        self.keys = []

    def set(self, key, data):
        index_key = hash(key) % len(self.hashtable)  # bucket index
        self.hashtable[index_key].insert([key, data])
        self.size += 1
        self.keys.append(key)

    def get(self, key):
        index_key = hash(key) % len(self.hashtable)
        return self.hashtable[index_key].return_data(key)

    def update(self, key, data):
        index_key = hash(key) % len(sef.hashtable)
        self.hashtable[index_key].find(key).data[1] = data

    def get_keys(self):
        return self.keys

    def get_values(self):
        values = []
        for key in self.keys:
            values.append(self.get(key))
        return values


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head  # top node in the list

    def append(self, data):  # takes data and inits new node
        new_node = Node(data)  # adds new_node to the list
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head  # starts at the first node and counts
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def find(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data is not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
