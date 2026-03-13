def copy_stack(original):
    temp = Stack()
    copy = Stack()

    # Step 1: reverse into temp
    while not original.is_empty():
        temp.push(original.pop())

    # Step 2: restore original + build copy
    while not temp.is_empty():
        item = temp.pop()
        original.push(item)
        copy.push(item)

    return copy
