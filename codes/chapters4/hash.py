# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/6/8 14:49 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
# @Summary : 哈希表

print("============================== 哈希 ==============================")
from typing import Dict, Optional

# 初始化哈希表
mapp: Dict = {}

# 添加操作
# 在哈希表中添加键值对 (key, value)
mapp[12836] = "小哈"
mapp[15937] = "小啰"
mapp[16750] = "小算"
mapp[13276] = "小法"
mapp[10583] = "小鸭"

# 查询操作
# 向哈希表输入键 key ，得到值 value
name: str = mapp[15937]
print(name)

# 删除操作
# 在哈希表中删除键值对 (key, value)
mapp.pop(10583)

# 遍历哈希表
# 遍历键值对 key->value
for key, value in mapp.items():
    print(key, "->", value)
# 单独遍历键 key
for key in mapp.keys():
    print(key)
# 单独遍历值 value
for value in mapp.values():
    print(value)

print("============================== 哈希 ==============================")
print("============================== 哈希函数示例 ==============================")


class Entry:
    """键值对 int->String"""

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val


class ArrayHashMap:
    """基于数组简易实现的哈希表"""

    def __init__(self):
        """构造方法"""
        # 初始化数组，包含 100 个桶
        self.buckets: list[Optional[Entry]] = [None] * 100

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        index = key % 100
        return index

    def get(self, key: int) -> Optional[str]:
        """查询操作"""
        index: int = self.hash_func(key)
        pair: Entry = self.buckets[index]
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str) -> None:
        """添加操作"""
        pair = Entry(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int) -> None:
        """删除操作"""
        index: int = self.hash_func(key)
        # 置为 None ，代表删除
        self.buckets[index] = None

    def entry_set(self) -> list[Entry]:
        """获取所有键值对"""
        result: list[Entry] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self) -> list[int]:
        """获取所有键"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self) -> list[str]:
        """获取所有值"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result

    def print(self) -> None:
        """打印哈希表"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)


# 创建一个新的哈希表
hash_map = ArrayHashMap()

# 插入一些键值对
hash_map.put(1, 'One')
hash_map.put(2, 'Two')
hash_map.put(3, 'Three')

# 打印哈希表的内容
hash_map.print()
# 输出：
# 1 -> One
# 2 -> Two
# 3 -> Three

# 获取特定键的值
print(hash_map.get(1))  # 输出: One
print(hash_map.get(2))  # 输出: Two
print(hash_map.get(1001))  # 输出: One 哈希冲突

# 删除键
hash_map.remove(1)
hash_map.print()
# 输出：
# 2 -> Two
# 3 -> Three

# 获取所有的键和值
print(hash_map.key_set())  # 输出: [2, 3]
print(hash_map.value_set())  # 输出: ['Two', 'Three']

# 获取所有的键值对
entry_set = hash_map.entry_set()
for entry in entry_set:
    print(f'{entry.key} -> {entry.val}')
# 输出：
# 2 -> Two
# 3 -> Three

print("============================== 哈希函数示例 ==============================")
