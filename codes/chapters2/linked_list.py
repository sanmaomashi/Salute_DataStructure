# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/6/8 11:48 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
# @Summary : 链表

print("============================== 链表实现 ==============================")


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """插入新的节点"""
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def delete(self, data):
        """删除一个节点"""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

    def print_list(self):
        """打印链表"""
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


# 创建一个链表并插入节点
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# 打印链表
linked_list.print_list()  # 输出: 1 2 3 4

# 删除节点
linked_list.delete(3)

# 再次打印链表
linked_list.print_list()  # 输出: 1 2 4

print("============================== 链表实现 ==============================")

print("============================== 链表查找 ==============================")


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """插入新的节点"""
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def delete(self, data):
        """删除一个节点"""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur = cur.next

    def search(self, data):
        """在链表中查找节点"""
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def print_list(self):
        """打印链表"""
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


# 创建一个链表并插入节点
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# 打印链表
linked_list.print_list()  # 输出: 1 2 3 4

# 搜索节点
print(linked_list.search(3))  # 输出: True
print(linked_list.search(5))  # 输出: False

print("============================== 链表查找 ==============================")
