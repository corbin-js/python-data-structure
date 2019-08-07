class ChainHashMap(HashMapBase):
    def put(self,key,value):
        _hash = self._hashfunction(key)
        if self._table[_hash] is None:
            self._table[_hash] = MapLinkedList()
        self._table[_hash].add(key,value)

    def get(self,key):
        _hash = self._hashfunction(key)
        if self._table[_hash] is None:
            raise "key 不存在"
        value=self._table[_hash].getValue(key)
        if value is None:
            raise "key 不存在"
        return value

    def setter(self,key,value):
        pass

    def delt(self,key):
        _hash = self._hashfunction(key)
        if self._table[_hash] is not None:
            self._table[_hash].remove(key)
    