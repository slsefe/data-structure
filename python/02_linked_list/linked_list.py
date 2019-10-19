"""
实现单链表的如下操作：
1. 初始化链表结点
2. 根据列表初始化链表
3. 判断链表是否为空
4. 获取链表长度
5. 按位置查询结点
6. 按值查询结点
7. 插入头结点
8. 插入尾结点
9. 指定位置之前插入结点
10. 指定位置之后插入节点
11. 按位置删除节点
12. 按值删除节点
"""
from typing import List


# 单链表结点类
class Node:

    def __init__(self, value: int, next_node=None):
        self.val = value
        self.next = next_node


# 单链表类
class SinglyLinkedList:

    # 初始化单链表
    def __init__(self):
        self.head = None
        self.num = 0  # num记录结点数

    # 使用列表类型的data创建链表
    def create_with_list(self, data: List[int]):
        # 将第一个值赋给头结点,当前指针p指向头结点
        self.head = Node(data[0])
        p = self.head
        # 创建指针指向顺序
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    # 判断链表是否为空
    def is_empty(self) -> bool:
        return self.head is None

    # 获取链表长度
    def get_length(self) -> int:
        return self.num

    def find_by_index(self, index: int) -> Node:
        """search node by index"""
        p = self.head
        i = 0
        while p and i != index:
            p = p.next
            i += 1
        return p

    def find_by_value(self, value: int) -> Node:
        """search node by value"""
        p = self.head
        while p and p.val != value:
            p = p.next
        return p

    def insert_to_head(self, value: int):
        if self.is_empty():
            self.head = Node(value)
        else:
            p = Node(value)
            p.next = self.head
            self.head = p

    def insert_to_tail(self, value: int):
        if self.is_empty():
            self.head = Node(value)
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = Node(value)

    def insert_after(self, index: int, value: int):
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        node = Node(value)
        node.next = p.next
        p.next = node

    def insert_before(self, index: int, value: int):
        self.insert_after(index-1, value)

    def delete_by_index(self, index: int) -> int:
        if index == 0:
            return self.delete_head()
        elif index == self.num - 1:
            return self.delete_tail()
        else:
            p = self.head
            i = 0
            while i < index-1:
                p = p.next
            e = p.next.val
            p.next = p.next.next
            return e

    def delete_head(self) -> int:
        if self.is_empty():
            return None
        else:
            e = self.head.val
            self.head = self.head.head
            return e

    def delete_tail(self) -> int:
        p = self.head
        while p.next and p.next.next:
            p = p.next
        e = p.next.val
        p.next = None
        return e

    def delete_by_value(self, value: int):
        p = self.head
        if p.val == value:
            self.delete_head()
        prev, p = p, p.next
        while p.val != value:
            prev = p
            p = p.next
        prev.next = p.next

    def __repr__(self) -> str:
        nums = []
        p = self.head
        while p:
            nums.append(p.val)
            p = p.next
        return "->".join(str(num) for num in nums)

    # 使链表支持迭代器操作
    def __iter__(self):
        p = self.head
        while p:
            yield p.value
            p = p.next

    def clear_list(self):
        self.head = None
        self.num = 0

    def print_all(self):
        p = self.head
        if p:
            print(f"{p.val}", end="")
            p = p.next
        while p:
            print(f"->{p.val}", end="")
            p = p.next
        print("\n", flush=True)

    # 对表中的所有元素执行proc操作
    def map(self, proc):
        p = self.head
        while p is not None:
            proc(p.value)
            p = p.next
