class Stack:
    """ LIFO """

    def __init__(self):
        self.__container = []

    
    def add(self, el):
        self.__container.append(el)

    def remove(self):
        if len(self.__container) == 0:
            raise IndexError("Stack is empty.")
        return self.__container.pop()

    def __eq__(self, el):
        if type(el) == list:
            return self.__container == el
        return self == el

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(self.__container)


class Queue:
    """ FIFO """

    def __init__(self):
        self.__container = []

    def add(self, el):
        self.__container.append(el)

    def remove(self):
        if len(self.__container) == 0:
            raise IndexError("Queue is empty.")
        fi = self.__container[0]
        self.__container = self.__container[1:]
        return fi

    def __eq__(self, el):
        if type(el) == list:
            return self.__container == el
        return self == el

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(self.__container)

class LinkedList:
    """ Class linked list """

    class Node:
        """ Put the node here. """

        def __init__(self, val):
            self.value = val
            self.next = None

        def __str__(self):
            return str(self.value)

        def __eq__(self, el):
            if type(el) == int:
                return self.value == el
            return self.value == el.value
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, el):
        n = self.Node(el)

        if not self.head and not self.tail:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n # type: ignore
            self.tail = n

        self.size += 1
        return n

    def remove(self):
        
        if not self.head:
            raise IndexError("Linked list is Empty")

        last = None

        if self.size == 1:
            last = self.head
            self.head = None
            self.tail = None

        else:
            curr = self.head
            last = self.tail
            new_last = None
            while curr.next:
                if curr.next == last:
                    new_last = curr
                    break
                curr = curr.next
            new_last.next = None # type: ignore
            self.tail = new_last

        self.size -= 1

        return last

    def remove_elem_by_index(self, index):
        """ Careful while using, if element is removed, index changes to. """
        if not self.head:
            raise IndexError("Linked list is Empty")

        curr = self.head
        i = 0

        if index == 0 and not self.head.next:
            print("Emptying the list.")
            self.head = None
            self.tail = None
        elif index == 0 and self.head.next:
            print("Removing first node.")
            self.head = self.head.next
        else:
            while curr.next:
                if i < index - 1:
                    i += 1
                    curr = curr.next
                    continue

                if curr.next == self.tail:
                    print("Removing end node.")
                    curr.next = None
                    self.tail = curr
                else:
                    print("Removing intermediate node.")
                    jump = curr.next.next
                    curr.next = jump
                break
        
        self.size -= 1

    def get(self, index):
        assert index >= 0
        assert type(index) == int

        if index >= self.size:
            raise IndexError("Index out of range")

        curr = self.head
        while curr.next and index > 0: # type: ignore
            index -= 1
            curr = curr.next # type: ignore

        return curr.value # type: ignore

    def find_first(self, value):
        """ First occurence only. """
        
        if self.size == 0:
            return

        if self.head.value == value: # type: ignore
            return 0
        
        index = 0
        curr = self.head
        while curr.next: # type: ignore
            index += 1
            curr = curr.next # type: ignore
            if curr.value == value:
                return index
        
        return

    def __len__(self):
        return self.size

    def __eq__(self, el):
        def _recursive_equal(el):
            _list = []
            curr = self.head
            while curr.next:    # type: ignore
                _list.append(curr.value) # type: ignore
                curr = curr.next # type: ignore
            _list.append(curr.value) # type: ignore
            return _list == el

        if type(el) == list:
            return _recursive_equal(el)

        return self == el

    def __str__(self):

        def __recursive_print():
            if not self.head:
                return "[]"
            s = "["
            curr = self.head
            while curr.next:
                s += (str(curr) + ', ')
                curr = curr.next
            s += f"{self.tail.value}]" # type: ignore
            return s
        
        return __recursive_print()