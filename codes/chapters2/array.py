# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/6/8 11:47 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
# @Summary : 数组


print("=" * 30 + "数组" + "=" * 30)
from typing import List
# 初始化数组
arr: List[int] = [0] * 5  # [ 0, 0, 0, 0, 0 ]
nums: List[int] = [1, 3, 2, 5, 4]


print(arr)
print(nums)
print("=" * 30 + "数组" + "=" * 30)

print("=" * 30 + "array" + "=" * 30)
import array

# 创建一个整数数组
arr = array.array('i', [1, 2, 3, 4, 5])

print(arr)  # 输出: array('i', [1, 2, 3, 4, 5])

# 访问数组元素
print(arr[0])  # 输出: 1

# 修改数组元素
arr[0] = 6
print(arr)  # 输出: array('i', [6, 2, 3, 4, 5])
print("=" * 30 + "array" + "=" * 30)

print("=" * 30 + "数组操作" + "=" * 30)

arr = [1, 2, 3, 4, 5]
arr.append(6)  # 将元素 6 插入数组的末尾
print(arr)
arr.remove(2)  # 将元素 2 从数组中删除
print(arr)
first_element = arr[0]  # 访问数组的第一个元素
print(first_element)

print("--------------")


def traverse(nums):
    """遍历数组"""
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        print(nums[i])
        count += 1
    print("--------------")
    # 直接遍历数组
    for num in nums:
        print(num)
        count += 1
    print("--------------")
    # 同时遍历数据索引和元素
    for i, num in enumerate(nums):
        print(i, num)
        count += 1


traverse(arr)
print("--------------")


def find(nums, target: int) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


print(find(arr, 1))

print("=" * 30 + "数组操作" + "=" * 30)
