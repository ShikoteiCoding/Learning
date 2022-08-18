

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

    def __str__(self):
        return str(self.__container)