# AVL 树 

## 一、概述

在二叉搜索树章节中，我们提到了在多次插入和删除操作后，二叉搜索树可能退化为链表。这种情况下，所有操作的时间复杂度将从 $O(\log n)$ 恶化为 $O(n)$。

如下图所示，经过两次删除节点操作，这个二叉搜索树便会退化为链表。

![AVL 树在删除节点后发生退化](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/90.png)

再例如，在以下完美二叉树中插入两个节点后，树将严重向左倾斜，查找操作的时间复杂度也随之恶化。

![AVL 树在插入节点后发生退化](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/91.png)

G. M. Adelson-Velsky 和 E. M. Landis 在其 1962 年发表的论文 "An algorithm for the organization of information" 中提出了「AVL 树」。论文中详细描述了一系列操作，确保在持续添加和删除节点后，AVL 树不会退化，从而使得各种操作的时间复杂度保持在 $O(\log n)$ 级别。换句话说，在需要频繁进行增删查改操作的场景中，AVL 树能始终保持高效的数据操作性能，具有很好的应用价值。

## 二、AVL 树常见术语

「AVL 树」既是二叉搜索树也是平衡二叉树，同时满足这两类二叉树的所有性质，因此也被称为「平衡二叉搜索树」。

### 1. 节点高度

在操作 AVL 树时，我们需要获取节点的高度，因此需要为 AVL 树的节点类添加 `height` 变量。

```python
class TreeNode:
    """AVL 树节点类"""
    def __init__(self, val: int):
        self.val: int = val                    # 节点值
        self.height: int = 0                   # 节点高度
        self.left: Optional[TreeNode] = None   # 左子节点引用
        self.right: Optional[TreeNode] = None  # 右子节点引用
```

「节点高度」是指从该节点到最远叶节点的距离，即所经过的“边”的数量。需要特别注意的是，叶节点的高度为 0 ，而空节点的高度为 -1 。我们将创建两个工具函数，分别用于获取和更新节点的高度。

```python
def height(self, node: TreeNode | None) -> int:
    """获取节点高度"""
    # 空节点高度为 -1 ，叶节点高度为 0
    if node is not None:
        return node.height
    return -1

def __update_height(self, node: TreeNode | None):
    """更新节点高度"""
    # 节点高度等于最高子树高度 + 1
    node.height = max([self.height(node.left), self.height(node.right)]) + 1
```

### 2. 节点平衡因子

节点的「平衡因子 Balance Factor」定义为节点左子树的高度减去右子树的高度，同时规定空节点的平衡因子为 0 。我们同样将获取节点平衡因子的功能封装成函数，方便后续使用。


~~~python
def balance_factor(self, node: TreeNode | None) -> int:
    """获取平衡因子"""
    # 空节点平衡因子为 0
    if node is None:
        return 0
    # 节点平衡因子 = 左子树高度 - 右子树高度
    return self.height(node.left) - self.height(node.right)
~~~

!>设平衡因子为 $f$ ，则一棵 AVL 树的任意节点的平衡因子皆满足 $-1 \le f \le 1$ 。

## 三、AVL 树旋转

AVL 树的特点在于「旋转 Rotation」操作，它能够在不影响二叉树的中序遍历序列的前提下，使失衡节点重新恢复平衡。换句话说，**旋转操作既能保持树的「二叉搜索树」属性，也能使树重新变为「平衡二叉树」**。

我们将平衡因子绝对值 $> 1$ 的节点称为「失衡节点」。根据节点失衡情况的不同，旋转操作分为四种：右旋、左旋、先右旋后左旋、先左旋后右旋。下面我们将详细介绍这些旋转操作。

### 1. 右旋

如下图所示，节点下方为平衡因子。从底至顶看，二叉树中首个失衡节点是“节点 3”。我们关注以该失衡节点为根节点的子树，将该节点记为 `node` ，其左子节点记为 `child` ，执行「右旋」操作。完成右旋后，子树已经恢复平衡，并且仍然保持二叉搜索树的特性。

<!-- tabs:start -->

#### **Step 1**

![右旋操作步骤](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/92.png)

#### **Step 2**

![avltree_right_rotate_step2](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/93.png)

#### **Step 3**

![avltree_right_rotate_step3](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/94.png)

#### **Step 4**

![avltree_right_rotate_step4](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/95.png)

<!-- tabs:end -->


此外，如果节点 `child` 本身有右子节点（记为 `grandChild` ），则需要在「右旋」中添加一步：将 `grandChild` 作为 `node` 的左子节点。

![有 grandChild 的右旋操作](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/96.png)

“向右旋转”是一种形象化的说法，实际上需要通过修改节点指针来实现，代码如下所示。

```python
def __right_rotate(self, node: TreeNode | None) -> TreeNode | None:
    """右旋操作"""
    child = node.left
    grand_child = child.right
    # 以 child 为原点，将 node 向右旋转
    child.right = node
    node.left = grand_child
    # 更新节点高度
    self.__update_height(node)
    self.__update_height(child)
    # 返回旋转后子树的根节点
    return child
```

### 2. 左旋

相应的，如果考虑上述失衡二叉树的“镜像”，则需要执行「左旋」操作。

![左旋操作](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/97.png)

同理，若节点 `child` 本身有左子节点（记为 `grandChild` ），则需要在「左旋」中添加一步：将 `grandChild` 作为 `node` 的右子节点。

![有 grandChild 的左旋操作](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/98.png)

可以观察到，**右旋和左旋操作在逻辑上是镜像对称的，它们分别解决的两种失衡情况也是对称的**。基于对称性，我们可以轻松地从右旋的代码推导出左旋的代码。具体地，只需将「右旋」代码中的把所有的 `left` 替换为 `right` ，将所有的 `right` 替换为 `left` ，即可得到「左旋」代码。

```python
def __left_rotate(self, node: TreeNode | None) -> TreeNode | None:
    """左旋操作"""
    child = node.right
    grand_child = child.left
    # 以 child 为原点，将 node 向左旋转
    child.left = node
    node.right = grand_child
    # 更新节点高度
    self.__update_height(node)
    self.__update_height(child)
    # 返回旋转后子树的根节点
    return child
```

### 3. 先左旋后右旋

对于下图中的失衡节点 3，仅使用左旋或右旋都无法使子树恢复平衡。此时需要先左旋后右旋，即先对 `child` 执行「左旋」，再对 `node` 执行「右旋」。

![先左旋后右旋](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/99.png)

### 4. 先右旋后左旋

同理，对于上述失衡二叉树的镜像情况，需要先右旋后左旋，即先对 `child` 执行「右旋」，然后对 `node` 执行「左旋」。

![先右旋后左旋](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/100.png)

### 5. 旋转的选择

下图展示的四种失衡情况与上述案例逐个对应，分别需要采用右旋、左旋、先右后左、先左后右的旋转操作。

![AVL 树的四种旋转情况](/Users/zhougaofeng/Desktop/Salute_系列/Salute_DataStructure/img/101.png)

在代码中，我们通过判断失衡节点的平衡因子以及较高一侧子节点的平衡因子的正负号，来确定失衡节点属于上图中的哪种情况。

| 失衡节点的平衡因子 | 子节点的平衡因子 | 应采用的旋转方法 |
| ------------------ | ---------------- | ---------------- |
| $>0$ （即左偏树）  | $\geq 0$         | 右旋             |
| $>0$ （即左偏树）  | $<0$             | 先左旋后右旋     |
| $<0$ （即右偏树）  | $\leq 0$         | 左旋             |
| $<0$ （即右偏树）  | $>0$             | 先右旋后左旋     |

为了便于使用，我们将旋转操作封装成一个函数。**有了这个函数，我们就能对各种失衡情况进行旋转，使失衡节点重新恢复平衡**。

```python
def __rotate(self, node: TreeNode | None) -> TreeNode | None:
    """执行旋转操作，使该子树重新恢复平衡"""
    # 获取节点 node 的平衡因子
    balance_factor = self.balance_factor(node)
    # 左偏树
    if balance_factor > 1:
        if self.balance_factor(node.left) >= 0:
            # 右旋
            return self.__right_rotate(node)
        else:
            # 先左旋后右旋
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)
    # 右偏树
    elif balance_factor < -1:
        if self.balance_factor(node.right) <= 0:
            # 左旋
            return self.__left_rotate(node)
        else:
            # 先右旋后左旋
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)
    # 平衡树，无需旋转，直接返回
    return node
```

## 四、AVL 树常用操作

### 1. 插入节点

「AVL 树」的节点插入操作与「二叉搜索树」在主体上类似。唯一的区别在于，在 AVL 树中插入节点后，从该节点到根节点的路径上可能会出现一系列失衡节点。因此，**我们需要从这个节点开始，自底向上执行旋转操作，使所有失衡节点恢复平衡**。

```python
def insert(self, val) -> None:
    """插入节点"""
    self.__root = self.__insert_helper(self.__root, val)

def __insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
    """递归插入节点（辅助方法）"""
    if node is None:
        return TreeNode(val)
    # 1. 查找插入位置，并插入节点
    if val < node.val:
        node.left = self.__insert_helper(node.left, val)
    elif val > node.val:
        node.right = self.__insert_helper(node.right, val)
    else:
        # 重复节点不插入，直接返回
        return node
    # 更新节点高度
    self.__update_height(node)
    # 2. 执行旋转操作，使该子树重新恢复平衡
    return self.__rotate(node)
```

### 2. 删除节点

类似地，在二叉搜索树的删除节点方法的基础上，需要从底至顶地执行旋转操作，使所有失衡节点恢复平衡。


```python
def remove(self, val: int) -> None:
    """删除节点"""
    self.__root = self.__remove_helper(self.__root, val)

def __remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
    """递归删除节点（辅助方法）"""
    if node is None:
        return None
    # 1. 查找节点，并删除之
    if val < node.val:
        node.left = self.__remove_helper(node.left, val)
    elif val > node.val:
        node.right = self.__remove_helper(node.right, val)
    else:
        if node.left is None or node.right is None:
            child = node.left or node.right
            # 子节点数量 = 0 ，直接删除 node 并返回
            if child is None:
                return None
            # 子节点数量 = 1 ，直接删除 node
            else:
                node = child
        else:
            # 子节点数量 = 2 ，则将中序遍历的下个节点删除，并用该节点替换当前节点
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.right = self.__remove_helper(node.right, temp.val)
            node.val = temp.val
    # 更新节点高度
    self.__update_height(node)
    # 2. 执行旋转操作，使该子树重新恢复平衡
    return self.__rotate(node)
```

### 3. 查找节点

AVL 树的节点查找操作与二叉搜索树一致，在此不再赘述。

## 五、AVL 树典型应用

- 组织和存储大型数据，适用于高频查找、低频增删的场景；
- 用于构建数据库中的索引系统；

!>"为什么红黑树比 AVL 树更受欢迎？"</br>红黑树的平衡条件相对宽松，因此在红黑树中插入与删除节点所需的旋转操作相对较少，在节点增删操作上的平均效率高于 AVL 树。