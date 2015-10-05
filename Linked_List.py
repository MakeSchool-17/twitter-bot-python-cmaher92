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
    # 
    # def __str__(self):
    #     return_str = ''
    #     current_node = self.head
    #     while current_node is not None:
    #         return_str += str(current_node.data) + ' '
    #         current_node = current_node.next_node
    #     return return_str
