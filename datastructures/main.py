from arrays import Stack, Queue, LinkedList


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

    print(f"After adding 3 elements: {l}")

    removed = l.remove()

    print(f"After removing one element: {l}, removed element is ({removed}), new size is {l.size}")

    removed = l.remove()
    removed = l.remove()

    print(f"After removing all elements: {l}, removed element is ({removed}), new size is {l.size}")

    try:
        l.remove()
    except:
        print(f"Empty LinkedList: {l}")

if __name__ == "__main__":
    print("Examples go here")

    test_linked_list()