from timeit import Timer


def get_average_time(stmt, setup='pass'):
    """Calculate the average time for 1 execution in microseconds."""

    timer = Timer(stmt=stmt, setup=setup, globals=globals())
    results = timer.autorange()

    return results[1] / results[0] * 1_000_000


def print_list_runtimes():
    """Print average runtimes for list methods"""

    setup_empty = 'lst = []'
    setup_full = 'lst = [0 for _ in range(10_000_000)]'

    res = get_average_time('lst[-1]', setup_full)
    print(f'list indexing: {res} microseconds')

    res = get_average_time('lst.append(1)', setup_empty)
    print(f'list appending: {res} microseconds')

    res = get_average_time('lst.pop()', setup_full)
    print(f'list popping from end: {res} microseconds')

    res = get_average_time('lst.insert(0, -1)', setup_full)
    print(f'list inserting at front: {res} microseconds')

    res = get_average_time('lst.pop(0)', setup_full)
    print(f'list popping from front: {res} microseconds')


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        self.length += 1

        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def appendleft(self, data):
        new_node = Node(data)
        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.tail is None:
            raise IndexError('pop from empty list')

        data = self.tail.data
        self.length -= 1

        if self.tail is self.head:
            self.head = None
            self.tail = None

        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current

        return data

    def popleft(self):
        if self.head is None:
            raise IndexError('pop from empty list')

        data = self.head.data
        self.length -= 1

        if self.head is self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next

        return data

    def get_by_index(self, index):
        counter = 0
        current = self.head
        while counter < index and current is not None:
            counter += 1
            current = current.next

        if current is None or index < 0:
            raise IndexError('list index out of range')

        return current.data


class DoubleLinkedList(LinkedList):
    def append(self, data):
        new_node = DoubleNode(data)
        self.length += 1

        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def appendleft(self, data):
        new_node = DoubleNode(data)
        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        if self.tail is None:
            raise IndexError('pop from empty list')

        data = self.tail.data
        self.length -= 1

        if self.tail is self.head:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def popleft(self):
        if self.head is None:
            raise IndexError('pop from empty list')

        data = self.head.data
        self.length -= 1

        if self.head is self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None

        return data


def setup_ll(length, single):
    """Initialize a full LinkedList for timing."""

    if single:
        lst = LinkedList()
    else:
        lst = DoubleLinkedList()

    for _ in range(length):
        lst.append(0)

    return lst


def print_ll_runtimes(single=True):
    """Print average runtimes for LinkedList methods"""

    if single:
        setup_empty = 'll = LinkedList()'
        print('Singly linked list')
    else:
        setup_empty = 'll = DoubleLinkedList()'
        print('Doubly linked list')

    setup_full = f'll = setup_ll(2_000_000, {single})'

    res = get_average_time('ll.append(0)', setup_empty)
    print(f'LL appending to end: {res} microseconds')

    res = get_average_time('ll.pop()', setup_full)
    print(f'LL popping from end: {res} microseconds')

    res = get_average_time('ll.appendleft(0)', setup_empty)
    print(f'LL inserting at front: {res} microseconds')

    res = get_average_time('ll.popleft()', setup_full)
    print(f'LL popping from front: {res} microseconds')

    res = get_average_time('ll.get_by_index(1_999_999)', setup_full)
    print(f'LL getting by index: {res} microseconds')
