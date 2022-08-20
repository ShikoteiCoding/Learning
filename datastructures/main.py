from arrays import Stack, Queue, LinkedList
from graphs import AdjacencyMatrix, AdjacencyList

import utils

def test_stack():
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)

    print(f"After adding 3 element: {s}")
    s.remove()
    print(f"After removing one element: {s}")
    s.remove()
    s.remove()
    print(f"After removing everything: {s}")
    try:
        s.remove()
    except:
        print("Empty Stack")

def test_queue():
    q = Queue()

    q.add(1)
    q.add(2)
    q.add(3)

    print(f"After adding 3 elements: {q}")
    removed = q.remove()
    print(f"After removing one element: {q}, removed element is {removed}")
    q.remove()
    q.remove()
    print(f"After removing everything: {q}")
    try:
        q.remove()
    except:
        print("Empty Queue")

def test_linked_list():
    l = LinkedList()

    print(f"Empty linked list {l}")

    l.add(1)
    l.add(2)
    l.add(3)

    pos = l.find_first(3)
    print(f"Find position of value 3: {pos}")

    print(f"After adding 3 elements: {l}")

    print(f"Getting the element of iteratively: {[l.get(i) for i in range(0, l.size)]} with size = {l.size}")
    removed = l.remove()

    print(f"After removing one element: {l}, removed element is ({removed}), new size is {l.size}")


    removed = l.remove()
    removed = l.remove()

    print(f"After removing all elements: {l}, removed element is ({removed}), new size is {l.size}")

    try:
        l.remove()
    except:
        print(f"Empty LinkedList: {l}")

def test_adjacency_matrix():
    a = AdjacencyMatrix()

    [a.add_vertex() for _ in range(4)]

    a.add_edge(0, 1)
    a.add_edge(2, 0)

    a.remove_edge(3, 0)
    a.remove_edge(2, 0)

    print(a) 

def test_adjacency_list():
    utils.print_banner("Testing Not Directed Adjacency List")
    a = AdjacencyList(directed=False)

    for _ in range(4): a.add_vertex()

    a.add_edge(0, 1)
    a.add_edge(2, 0)
    a.add_edge(3, 0)
    a.add_edge(3, 1)
    a.add_edge(3, 2)
    a.add_edge(3, 2)    # already connected
    a.add_edge(2, 3)    # already connected

    print(a)

    a.remove_edge(3, 0)
    a.remove_edge(2, 0)
    a.remove_edge(2, 1)

    print(a)

def test_adjacency_directed_list():
    utils.print_banner("Testing Directed Adjacency List")
    a = AdjacencyList(directed=True)

    for _ in range(4): a.add_vertex()

    a.add_edge(0, 1)
    a.add_edge(2, 0)
    a.add_edge(3, 0)
    a.add_edge(3, 1)
    a.add_edge(3, 2)
    a.add_edge(3, 2)    # already connected
    a.add_edge(2, 3)    # already connected

    print(a)

if __name__ == "__main__":
    print("Examples go here:\n")

    test_adjacency_list()
    test_adjacency_directed_list()