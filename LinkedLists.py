class Node:
    def __init__(self, element = None):
        self.element = element
        self.next = None
        self.previous = None
    def __str__(self):
        node_string = "[{}]".format(self.element)
        if self.next != None:
            node_string += " -> "
        return node_string

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, element):
        node = Node(element)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove(self, element):
        """Remove the first instance of this element from the list. If element
           is not in the list, do nothing."""
        if not self.is_empty():
            if self.size == 1 and self.head.element == element:
                self.head = None
                self.tail = None
                self.size = 0
                return
            current = self.head
            while current != self.tail:
                # current will never be tail in the loop
                if current == self.head and self.head.element == element:
                    # need to remove the head
                    self.head = self.head.next
                    self.size -= 1
                    return
                elif current.next == self.tail and self.tail.element == element:
                    # need to remove the tail, current points to the node before
                    # the tail
                    self.tail = current
                    self.tail.next = None
                    self.size -= 1
                    return
                elif current.element == element:
                    # the element to remove is in the middle of the list
                    p.next = current.next # skip over it
                    self.size -= 1
                    return
                p = current
                current = current.next

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            current = self.head
            list_string = str(current)
            while current != self.tail:
                current = current.next
                list_string += str(current)
            return list_string

    def contains(self, num):
        if not self.is_empty():
            currentNode = self.head
            while True:
                if currentNode.element == num:
                    return True
                else:
                    currentNode = currentNode.next
                if(currentNode == None):
                    return False
        return False

    def prepend(self, node):

        if(self.is_empty()):
            self.append(node)
            return
        nodeN = Node(node)
        nodeN.next = self.head
        self.head = nodeN
        self.size += 1

    def join(self, lst):
        if(lst.is_empty()):
            return
        if(self.is_empty()):
            currentNode = lst.head
            while True:
                self.append(currentNode.element)
                currentNode = currentNode.next
                if(currentNode == None):
                    break
            return

        self.tail.next = lst.head
        self.tail = lst.tail
        self.size = self.size + lst.size

##################################################

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __repr__(self):
        string = ""

        if (self.head == None):
            string += "Doubly Linked List Empty"
            return string

        string += f"Doubly Linked List:\n{self.head.data}"
        start = self.head.next
        while (start != None):
            string += f" -> {start.data}"
            start = start.next
        return string

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
            return

        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.count += 1

    def insert(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        if (index == self.count):
            self.append(data)
            return

        if (index == 0):
            self.head.previous = Node(data)
            self.head.previous.next = self.head
            self.head = self.head.previous
            self.count += 1
            return

        start = self.head
        for _ in range(index):
            start = start.next
        start.previous.next = Node(data)
        start.previous.next.previous = start.previous
        start.previous.next.next = start
        start.previous = start.previous.next
        self.count += 1
        return

    def remove(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return

        if index == (self.count - 1):
            self.tail = self.tail.previous
            self.tail.next = None
            self.count -= 1
            return

        start = self.head
        for i in range(index):
            start = start.next
        start.previous.next, start.next.previous = start.next, start.previous
        self.count -= 1
        return

    def index(self, data):
        start = self.head
        for i in range(self.count):
            if (start.data == data):
                return i
            start = start.next
        return None

    def size(self):
        return self.count

    def display(self):
        print(self)

