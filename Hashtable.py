class Hashtable:
    def __init__(self):
        basic_table = ['A', 1, 'B', 2, 'C', 3, 'D', 4]

    def get(key, assoc_array):
        value = None
        for index, item in enumerate(assoc_array):
            if item == key:
                value = assoc_array[index + 1]
                break
        return value
