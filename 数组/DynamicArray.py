class DynamicArray:
    def __init__(self):
        #数组长度
        self._length=0
        #数组容量
        self._capacity=10
        #数组内容
        self._context=[None]*self._capacity
        
    def getLen(self):
        return self._length
    
    def add(self,item):
        self._checkExtend()
        self._context[self._length]=item
        self._length+=1
    
    def remove(self,item):
        for i in range(self._length):
            if self._context[i] == item:
                for j in range(i, self._length - 1): #一个个移上来
                    self._context[j]=self._context[j+1]
                self._length-=1
                break
                
    def insert(self,index,item):
        self._checkExtend()
        for i in range(self._length,index,-1):#一个个往后移
            self._context[i]=self._context[i-1]
        self._context[index]=item
        self._length+=1
    
    def index(self,item):
        for i in range(self._length):
            if self._context[i] == item:
                return i
                break
        
        return -1
    
    def _checkExtend(self):#检查数组大小是否撑满
        if self._length+1==self._capacity:
            #此处扩展数组长度，每次扩展一倍
            self._capacity *= 2
            __c =[None]*self._capacity
            for i in range(self._length):
                __c[i]=self._context[i]
            self._context=__c
    
    def print(self):
        for i in range(self._length):
            print(self._context[i] ,end = " ")