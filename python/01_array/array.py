#!usr/bin/python
"""
实现数组的根据下标随机访问、插入、删除操作。
"""


class Array:

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            self._data.insert(index, value)
            return True

    def print_all(self):
        for item in self:
            print(item)


def my_test_array():
    array = Array(5)
    assert len(array) == 0  # 数组初始长度为0
    assert array.delete(0) is False  # 空数组不能删除
    array.insert(0, 4)  # 插入元素
    assert len(array) == 1  # 插入元素使数组长度加1
    assert array.find(0) == 4  # 是否插入到正确的位置
    array.insert(0, 2)
    assert len(array) == 2  # 插入元素使数组长度加1
    assert array.find(0) == 2  # 插入操作是否正确
    assert array.find(1) == 4  # 插入操作是否正确
    array.insert(1, 3)
    array.insert(3, 5)
    array.insert(0, 1)
    array.print_all()  # 1,2,3,4,5
    assert array.insert(0, 100) is False  # 数组满时不能再插入元素
    assert len(array) == 5
    assert array.find(0) == 1
    assert array.find(1) == 2
    assert array.find(2) == 3
    assert array.find(3) == 4
    assert array.find(4) == 5
    assert array.delete(5) is False  # 不能删除非法位置的元素
    assert array.delete(3) is True  # 可以删除合法位置的元素
    assert len(array) == 4  # 删除操作使数组长度减1
    assert array.find(3) == 5  # 删除指定元素后后面元素向前移动
    array.print_all()  # 1,2,3,5


if __name__ == "__main__":
    my_test_array()
