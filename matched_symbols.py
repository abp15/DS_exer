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



def matched_symbols(symbol_string):
    symbol_pairs = { '(' : ')',
                    '{' : '}',
                    '[' : ']'
                  }
    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_string):
        symbol = symbol_string[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:  # The symbol is a closer

            # If the Stack is already empty, the symbols are not balanced
            if my_stack.is_empty():
                return False

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True

    return False  # Stack is not empty so symbols were not balanced

print(matched_symbols('([{}])'))
print(matched_symbols('(([{}]])'))
