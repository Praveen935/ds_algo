class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class List(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return

        curr = self.head
        pre = None
        while curr:
            pre = curr
            curr = curr.next

        pre.next = node

    def insert(self, value):
        pass

    def display(self):
        if not self.head:
            print('Not elemnet')
            return
        curr = self.head
        while curr is not None:
            print('%s' %curr.value)
            curr = curr.next

    def search(self, value):
        if not self.head:
            return None
        curr = self.head

        while curr:
            if curr.value == value:
                return curr
            curr = curr.next

        return None




