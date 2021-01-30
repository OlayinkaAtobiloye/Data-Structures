class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    """A linked list is a linear data structure. It consists of nodes. Each Node has a value and a pointer
    to a neighbouring node(i.e it links to it's neighbor) hence the name linked list.
    They are used in cases where constant time insertion and deletion are required."""
    def __init__(self, head=None):
        self.head = head

    def insert(self, value, position):
        count = 0
        current = self.head
        while current:
            previous = current
            current = current.next
            count += 1
            if count == position:
                previous.next = value
                value.next = current
                break

    def append(self, value):
        """takes in the head of the linked list and the value to be appended in the linked list. """
        current = self.head
        previous = current
        if current:
            while current:
                previous = current
                current = current.next
            else:
                previous.next = value
        else:
            self.head = value

    def remove(self, position):
        """removes element at given position"""
        current = self.head
        count = 0
        if current:
            while current:
                previous = current
                current = current.next
                count += 1
                if count == position:
                    previous.next = current.next
                    break

    def pop(self):
        """removes the last element from the linked list. """
        current = self.head
        previous = current
        last = previous
        while current:
            last = previous
            previous = current
            current = current.next
        else:
            last.next = None

    def __repr__(self):
        """representation of the linked list"""
        x = self.head
        a = f'{str(x.value)}'
        if x:
            while x.next:
                x = x.next
                a += f"-->{str(x.value)}"
        return a


l = LinkedList(Node(6))
l.append(Node(5))
l.append(Node(7))
l.append(Node(10))
l.append(Node(1))
l.append(Node(3))
l.insert(Node(8), 2)
l.append(Node(9))
l.remove(3)
# print(l.head.value)
# print(l.head.next.value)
print(l)

