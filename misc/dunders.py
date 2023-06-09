class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_nodes(self):
        current = self.head

        while current:
            print(current.data, end='-> ')
            current = current.next

        print()

    def _calc_length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def __len__(self):
        return self._calc_length()

    def __add__(self, other_ll):
        new_ll = LinkedList()

        current = self.head

        while current:
            new_ll.append(current.data)
            current = current.next

        current = other_ll.head

        while current:
            new_ll.append(current.data)
            current = current.next

        return new_ll
