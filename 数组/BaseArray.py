class BaseArray(object):
    def __init__(self, size = 32):
        self.__size = size
        self.__items = [None] * size

    def __getitem__(self, item):
        # 判断是否越界，要先判断数组越界，越界可能为空
        if item > self.__size - 1:
            raise Exception('错误:数组越界')
        elif self.__items[item] is None:
            raise Exception('错误:数组在该位置没有被赋值')

        return self.__items[item]

    def __setitem__(self, key, value):
        # 判断越界
        if key > self.__size - 1:
            raise Exception('错误:数组越界')
        self.__items[key] = value

    def __iter__(self):
        for item in self.__items:
            yield item

    def __len__(self):
        return self.__size

    def clear(self, value = None):
        self.__items = [value for i in range(self.__size)]
        return

if __name__ == '__main__':
    a = BaseArray(10)
    for i in range(len(a)):
        a[i] = i

    # 测试赋值时数组越界
    try:
        temp = a[len(a) + 10]
        print('#temp#'+str(temp))
    except Exception as err:
        print(err)

    # 测试赋值时数组为空
    a[0] = None
    try:
        temp = a[0]
        print('#temp#'+str(temp))
    except Exception as err:
        print(err)

    # 测试set数组越界
    try:
        a[len(a) + 10] = 1234
        print('#a#', a[len(a) + 10])
    except Exception as err:
        print(err)


    print(list(a))

    a.clear(1)
    print(list(a))

    a.clear()
    print(list(a))
    