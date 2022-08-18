from arrays import Stack


def test_queue():
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
    s.remove()

if __name__ == "__main__":
    print("Examples go here")

    test_queue()