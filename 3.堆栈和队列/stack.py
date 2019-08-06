class ArrayStack():
    def __init__(self):
        self._stack=list()

    def isEmpty(self):
        return len(self._stack) == 0

    def push(self,value):
        self._stack.append(value)

    def pop(self):
        if not self.isEmpty():
            return self._stack.pop()
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self._stack[len(self._stack)-1]
        return None

    def print(self):
        print(self._stack)


class LinkedStack():
    def __init__(self):
        self._stack=LinkedList()

    def isEmpty(self):
        return len(self._stack)==0

    def push(self,value):
        self._stack.add_first(value)

    def pop(self):
        if not self.isEmpty():
            item=self._stack.removeIndex(0)
            return item.value
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self._stack.getItem(0)
        return None

    def print(self):
        self._stack.print()
