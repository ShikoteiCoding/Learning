from arrays import Stack, Queue


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

if __name__ == "__main__":
    print("Examples go here")

    test_queue()