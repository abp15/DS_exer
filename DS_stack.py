class Stack:


    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item and append it to the end of the list
           returns nothing
        """
        self.items.append(item)

        return

    def pop(self):
        """Remove and returns the last item from the stack
           Runtime for this method is O(1) or constant time.
           if no argument provided, pop will always give the last item in a list
        """
        if self.items:
            return self.items.pop()


    def peek(self):
        """Shows and returns the last item from the stack
           Runtime for this method is O(1) or constant time.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the length of the list that is representing the stack
           Runtime for this method is O(1) or constant time.
        """
        return len(self.items)


    def is_empty(self):
        """Returns True if the stack is empty
           Runtime for this method is O(1) or constant time.
        """
        if len(self.items) == 0:
            return True
        return False
