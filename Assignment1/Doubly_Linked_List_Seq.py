class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_Node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node

    def insert_last(self, x):
        new_Node = Doubly_Linked_List_Node(x)
        if self.tail is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.prev = self.tail
            self.tail.next = new_Node
            self.tail = new_Node

    def delete_first(self):
        # Make sure there is at least one node
        assert self.head
        x = self.head.item
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return x


    def delete_last(self):
        # Make sure there is at least one node
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if x1 == self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next
        if x2 == self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        x1.prev = None
        x2.next = None
        return L2

    def splice(self, x, L2):
        x1 = x.next
        x2 = L2.head
        x3 = L2.tail
        L2.head = None
        L2.tail = None
        x2.prev = x
        x.next = x2
        x3.next = x1
        if x1:
            x1.prev = x3
        else:
            self.tail = x3

