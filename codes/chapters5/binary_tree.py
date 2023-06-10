# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/6/10 10:07 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
# @Summary : 二叉树


from typing import Optional
from collections import deque


class TreeNode:
    """二叉树节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.left: Optional[TreeNode] = None  # 左子节点指针
        self.right: Optional[TreeNode] = None  # 右子节点指针


def preorder(node: Optional[TreeNode]):
    """前序遍历"""
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def inorder(node: Optional[TreeNode]):
    """中序遍历"""
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def postorder(node: Optional[TreeNode]):
    """后序遍历"""
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]


def level_order(root: Optional[TreeNode]):
    """层序遍历"""
    if root is None:
        return []
    queue: deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node: TreeNode = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res


# 用法示例：
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("前序遍历：", preorder(root))
print("中序遍历：", inorder(root))
print("后序遍历：", postorder(root))
print("层序遍历：", level_order(root))
