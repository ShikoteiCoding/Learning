

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