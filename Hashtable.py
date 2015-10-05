class Hashtable:
    def __init__(self):
        self.hashtable = []
        while len(self.hashtable) < 10:
            self.hashtable.append(LinkedList())
        self.size = 0
        self.keys = []

    def get_value(self, key, assoc_array):
        value = None
        for index, item in enumerate(assoc_array):
            if item == key:
                value = assoc_array[index + 1]
                break
        return value

    def get_keys(self):
        return self.keys
