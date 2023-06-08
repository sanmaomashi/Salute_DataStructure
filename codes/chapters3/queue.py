# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/6/8 14:21 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
# @Summary : 队列
from typing import Optional

print("============================== 队列 - 链表实现 ==============================")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        """检查队列是否为空"""
        return self.front is None

    def enqueue(self, item):
        """向队列添加元素"""
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        """从队列移除元素"""
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return str(temp.data)

    def peek(self):
        """获取队列的第一个元素"""
        if self.is_empty():
            return
        return str(self.front.data)


# 创建一个队列
q = Queue()

# 向队列添加元素
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# 获取队列的第一个元素
print(q.peek())  # 输出: 1

# 从队列移除元素
print(q.dequeue())  # 输出: 1
print(q.dequeue())  # 输出: 2
print(q.dequeue())  # 输出: 3

print("============================== 队列 - 链表实现 ==============================")

print("============================== 队列 - 数组实现 ==============================")


class ArrayQueue:
    """基于环形数组实现的队列"""

    def __init__(self, size: int) -> None:
        """构造方法"""
        self.__nums: list[int] = [0] * size  # 用于存储队列元素的数组
        self.__front: int = 0  # 队首指针，指向队首元素
        self.__size: int = 0  # 队列长度

    def capacity(self) -> int:
        """获取队列的容量"""
        return len(self.__nums)

    def size(self) -> int:
        """获取队列的长度"""
        return self.__size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self.__size == 0

    def push(self, num: int) -> None:
        """入队"""
        if self.__size == self.capacity():
            raise IndexError("队列已满")
        # 计算尾指针，指向队尾索引 + 1
        # 通过取余操作，实现 rear 越过数组尾部后回到头部F
        rear: int = (self.__front + self.__size) % self.capacity()
        # 将 num 添加至队尾
        self.__nums[rear] = num
        self.__size += 1

    def pop(self) -> int:
        """出队"""
        num: int = self.peek()
        # 队首指针向后移动一位，若越过尾部则返回到数组头部
        self.__front = (self.__front + 1) % self.capacity()
        self.__size -= 1
        return num

    def peek(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self.__nums[self.__front]

    def to_list(self) -> list[int]:
        """返回列表用于打印"""
        res = [0] * self.size()
        j: int = self.__front
        for i in range(self.size()):
            res[i] = self.__nums[(j % self.capacity())]
            j += 1
        return res


# 创建一个容量为5的队列
queue = ArrayQueue(5)

# 添加元素到队列
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.to_list())  # 输出: [1, 2, 3]

# 查看队列是否为空
print(queue.is_empty())  # 输出: False

# 查看队列的容量
print(queue.capacity())  # 输出: 5

# 查看队列的长度
print(queue.size())  # 输出: 3

# 查看队首元素
print(queue.peek())  # 输出: 1

# 出队
print(queue.pop())  # 输出: 1
print(queue.to_list())  # 输出: [2, 3]

# 再次入队
queue.push(4)
queue.push(5)
print(queue.to_list())  # 输出: [2, 3, 4, 5]

# 入队，由于队列已满，将抛出异常
try:
    queue.push(6)  # 抛出: IndexError: 队列已满
except IndexError as e:
    print(e)

print("============================== 队列 - 数组实现 ==============================")

print("============================== 双向队列 - 链表实现 ==============================")


class ListNode:
    """双向链表节点"""

    def __init__(self, val: int) -> None:
        """构造方法"""
        self.val: int = val
        self.next: Optional[ListNode] = None  # 后继节点引用（指针）
        self.prev: Optional[ListNode] = None  # 前驱节点引用（指针）


class LinkedListDeque:
    """基于双向链表实现的双向队列"""

    def __init__(self) -> None:
        """构造方法"""
        self.front: Optional[ListNode] = None  # 头节点 front
        self.rear: Optional[ListNode] = None  # 尾节点 rear
        self.__size: int = 0  # 双向队列的长度

    def size(self) -> int:
        """获取双向队列的长度"""
        return self.__size

    def is_empty(self) -> bool:
        """判断双向队列是否为空"""
        return self.size() == 0

    def push(self, num: int, is_front: bool) -> None:
        """入队操作"""
        node = ListNode(num)
        # 若链表为空，则令 front, rear 都指向 node
        if self.is_empty():
            self.front = self.rear = node
        # 队首入队操作
        elif is_front:
            # 将 node 添加至链表头部
            self.front.prev = node
            node.next = self.front
            self.front = node  # 更新头节点
        # 队尾入队操作
        else:
            # 将 node 添加至链表尾部
            self.rear.next = node
            node.prev = self.rear
            self.rear = node  # 更新尾节点
        self.__size += 1  # 更新队列长度

    def push_first(self, num: int) -> None:
        """队首入队"""
        self.push(num, True)

    def push_last(self, num: int) -> None:
        """队尾入队"""
        self.push(num, False)

    def pop(self, is_front: bool) -> Optional[int]:
        """出队操作"""
        # 若队列为空，直接返回 None
        if self.is_empty():
            return None
        # 队首出队操作
        if is_front:
            val: int = self.front.val  # 暂存头节点值
            # 删除头节点
            fnext: Optional[ListNode] = self.front.next
            if fnext != None:
                fnext.prev = None
                self.front.next = None
            self.front = fnext  # 更新头节点
        # 队尾出队操作
        else:
            val: int = self.rear.val  # 暂存尾节点值
            # 删除尾节点
            rprev: Optional[ListNode] = self.rear.prev
            if rprev != None:
                rprev.next = None
                self.rear.prev = None
            self.rear = rprev  # 更新尾节点
        self.__size -= 1  # 更新队列长度
        return val

    def pop_first(self) -> int:
        """队首出队"""
        return self.pop(True)

    def pop_last(self) -> int:
        """队尾出队"""
        return self.pop(False)

    def peek_first(self) -> int:
        """访问队首元素"""
        return None if self.is_empty() else self.front.val

    def peek_last(self) -> int:
        """访问队尾元素"""
        return None if self.is_empty() else self.rear.val

    def to_array(self) -> list[int]:
        """返回数组用于打印"""
        node = self.front
        res = [0] * self.size()
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res


# 创建一个双向队列
deque = LinkedListDeque()

# 向队首和队尾添加元素
deque.push_first(1)
deque.push_last(2)
print(deque.to_array())  # 输出: [1, 2]

# 查看双向队列是否为空
print(deque.is_empty())  # 输出: False

# 查看双向队列的长度
print(deque.size())  # 输出: 2

# 查看队首和队尾元素
print(deque.peek_first())  # 输出: 1
print(deque.peek_last())  # 输出: 2

# 队首和队尾出队
print(deque.pop_first())  # 输出: 1
print(deque.pop_last())  # 输出: 2
print(deque.to_array())  # 输出: []

# 再次向队首和队尾添加元素
deque.push_first(3)
deque.push_last(4)
print(deque.to_array())  # 输出: [3, 4]

print("============================== 双向队列 - 链表实现 ==============================")

print("============================== 双向队列 - 数组实现 ==============================")


class ArrayDeque:
    """基于环形数组实现的双向队列"""

    def __init__(self, capacity: int) -> None:
        """构造方法"""
        self.__nums: list[int] = [0] * capacity
        self.__front: int = 0
        self.__size: int = 0

    def capacity(self) -> int:
        """获取双向队列的容量"""
        return len(self.__nums)

    def size(self) -> int:
        """获取双向队列的长度"""
        return self.__size

    def is_empty(self) -> bool:
        """判断双向队列是否为空"""
        return self.__size == 0

    def index(self, i: int) -> int:
        """计算环形数组索引"""
        # 通过取余操作实现数组首尾相连
        # 当 i 越过数组尾部后，回到头部
        # 当 i 越过数组头部后，回到尾部
        return (i + self.capacity()) % self.capacity()

    def push_first(self, num: int) -> None:
        """队首入队"""
        if self.__size == self.capacity():
            print("双向队列已满")
            return
        # 队首指针向左移动一位
        # 通过取余操作，实现 front 越过数组头部后回到尾部
        self.__front = self.index(self.__front - 1)
        # 将 num 添加至队首
        self.__nums[self.__front] = num
        self.__size += 1

    def push_last(self, num: int) -> None:
        """队尾入队"""
        if self.__size == self.capacity():
            print("双向队列已满")
            return
        # 计算尾指针，指向队尾索引 + 1
        rear = self.index(self.__front + self.__size)
        # 将 num 添加至队尾
        self.__nums[rear] = num
        self.__size += 1

    def pop_first(self) -> int:
        """队首出队"""
        num = self.peek_first()
        # 队首指针向后移动一位
        self.__front = self.index(self.__front + 1)
        self.__size -= 1
        return num

    def pop_last(self) -> int:
        """队尾出队"""
        num = self.peek_last()
        self.__size -= 1
        return num

    def peek_first(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        return self.__nums[self.__front]

    def peek_last(self) -> int:
        """访问队尾元素"""
        if self.is_empty():
            raise IndexError("双向队列为空")
        # 计算尾元素索引
        last = self.index(self.__front + self.__size - 1)
        return self.__nums[last]

    def to_array(self) -> list[int]:
        """返回数组用于打印"""
        # 仅转换有效长度范围内的列表元素
        res = []
        for i in range(self.__size):
            res.append(self.__nums[self.index(self.__front + i)])
        return res


# 创建一个双向队列
deque = ArrayDeque(5)

# 向队首和队尾添加元素
deque.push_first(1)
deque.push_last(2)
print(deque.to_array())  # 输出: [1, 2]

# 查看双向队列是否为空
print(deque.is_empty())  # 输出: False

# 查看双向队列的长度
print(deque.size())  # 输出: 2

# 查看队首和队尾元素
print(deque.peek_first())  # 输出: 1
print(deque.peek_last())  # 输出: 2

# 队首和队尾出队
print(deque.pop_first())  # 输出: 1
print(deque.pop_last())  # 输出: 2
print(deque.to_array())  # 输出: []

# 再次向队首和队尾添加元素
deque.push_first(3)
deque.push_last(4)
print(deque.to_array())  # 输出: [3, 4]

print("============================== 双向队列 - 数组实现 ==============================")
