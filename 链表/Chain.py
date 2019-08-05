class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Chain(object):
    def __init__(self):
        self._size = 0
        self._root = Node()

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._root.next=None

    def add_first(self,value):
        node = Node(value)
        node.next=self._root.next
        self._root.next=node
        self._size+=1

    def add_last(self,value):
        node = Node(value)
        point=self._root
        while point.next is not None:
            point=point.next
        point.next=node
        self._size+=1

    def add(self,index,value):
        node = Node(value)
        point = self._root
        for i in range(index):
            point=point.next
        node.next=point.next
        point.next = node
        self._size+=1
        
    def remove(self,value):
        pre = self._root
        point = self._root.next
        while point is not None and point.value is not value:
            pre = point
            point = point.next
        if point is None:
            return None
        pre.next=point.next
        self._size-=1
        return point

    def getItem(self,index):
        point = self._root.next
        if(index>self._size):
            raise "越界"
        for i in range(index):
            point = point.next
        return point.value

    def getIndex(self,value):
        point = self._root.next
        n=0
        while n<self._size and point.value is not value:
            point = point.next
            n+=1
        if n==self._size:
            n=-1
        return n

    def print(self):
        if self._size==0:
            print('empty linked list')
        point = self._root.next
        while point is not None:
            print(point.value, end=" ")
            point=point.next
