class ArrayQueue():
    def __init__(self):
        #数组容量
        self._capacity=10
        #数组内容
        self._stack=[None]*self._capacity
        #head
        self._head=-1
        self._tail=-1

    def isEmpty(self):
        return self._head == -1

    def _resize(self):
        _stack=[None]*self._capacity*2
        for i in range(self._capacity):
            _stack[i]=self._stack[self._head]
            self._head=(self._head+1)%self._capacity
        self._tail=self._capacity
        self._capacity=self._capacity*2
        self._stack=_stack
        self._head=0

    def enqueue(self,value):
        self._tail=(self._tail+1)%self._capacity
        if self._stack[self._tail] is not None:
            self._resize()
        self._stack[self._tail]=value
        if self._head==-1:
            self._head=0

    def dequeue(self):
        if not self.isEmpty():
            value=self._stack[self._head]
            self._stack[self._head]=None
            self._head=(self._head+1)%self._capacity
            if self._stack[self._head] is None:
                self._head=self._tail=-1
            return value
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self._stack[self._head]
        return None

    def print(self):
        print(self._stack)


class LinkedQueue():
    def __init__(self):
        self._stack=LinkedList()

    def isEmpty(self):
        return len(self._stack)==0

    def enqueue(self,value):
        self._stack.add_last(value)

    def dequeue(self):
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