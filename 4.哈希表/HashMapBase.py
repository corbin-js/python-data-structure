class MapItem:
    def __init__(self,key=None,value=None):
        self._key=key
        self._value=value
        self._next=None

    def eq(self,key):
        return self._key == key


class MapLinkedList:
    def __init__(self):
        self._head=MapItem()
        self._tail=self._head

    def add(self,key,value):
        item=MapItem(key,value)
        self._tail._next=item
        self._tail=item

    def remove(self,key):
        pre=self._head
        pvt=self._head._next
        while pvt is not None and not pvt.eq(key):
            pre=pvt
            pvt=pvt._next
        if pvt is not None:
            pre._next=pvt._next

    def getValue(self,key):
        pvt=self._head._next
        while pvt is not None and not pvt.eq(key):
            pvt=pvt._next
        if pvt is not None:
            return pvt._value
        return None

    def print(self):
        pvt=self._head._next
        while pvt is not None:
            print(pvt._key,":",pvt._value,end="  |||  ")
            pvt=pvt._next

class HashMapBase:
    CAPACIYT = 10
    KEY = 127
    def __init__(self):
        self._table=[None] * HashMapBase.CAPACIYT

    def _hashfunction(self,key):
        _hash=0
        key=str(key)
        l=len(key)
        for i in range(l):
            _hash+=ord(key[i])*HashMapBase.KEY
        return self._rehash(_hash)

    def _rehash(self,_hash):
        return _hash%HashMapBase.CAPACIYT

    def print(self):
        for i in range(len(self._table)):
            print("第%d位" %(i),end=" => ")
            if self._table[i] is not None:
                self._table[i].print()
                print()
            else:
                print("第%d位为空" %(i))