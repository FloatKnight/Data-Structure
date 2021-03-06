# 二分搜索树集合
class BSTSet():
    class Node:
        def __init__(self, e=None, left=None, right=None):
            self.e = e
            self.left = left
            self.right = right

    def __init__(self):
        self.size = 0
        self.root = None

    #
    def getNode(self, e, node=-1):
        if node == -1: node = self.root
        if node == None: return None
        if node.e == e return node
        return self.getNode(e, node.left) if e < node.e else self.getNode(e, node.right)

    # 添加元素
    def add(self, e, node=-1):
        if node == -1:
            self.root = self.add(e, self.root)
            return
        if node == None:
            self.size += 1
            return self.Node(e)
        if e > node.e:
            node.right = self.add(e, node.right)
        elif e < node.e:
            node.left = self.add(e, node.left)
        return node

        # 找到最小的元素

    def minimum(self, node=-1):
        if self.size == 0: return
        if node == -1: node = self.root
        if node.left == None: return node.e
        return self.minimum(node.left)

    # 删除最小的元素
    def removeMin(self, node=-1):
        if self.size == 0: return
        if node == -1:
            node = self.root
            ret = self.minimum(node)
            self.root = self.removeMin(node)
            return ret
        if node.left == None:
            ret = node.right
            node.right = None
            self.size -= 1
            return ret
        node.left = self.removeMin(node.left)
        return node
        # 删除元素 e

    def remove(self, e, node=-1):
        if node == -1:
            self.root = self.remove(e, self.root)
            return
        if node == None: return
        if node.e == e:
            if node.right == None:
                self.size -= 1
                return node.left
            if node.left == None:
                self.size -= 1
                return node.right
            ret = self.Node(self.removeMax(node.left))
            ret.left, ret.right = node.left, node.right
            node.left = node.right = None
            return ret
        if e > node.e:
            node.right = self.remove(e, node.right)
        else:
            node.left = self.remove(e, node.left)
        return node

    # 是否包含元素
    def contains(self, e, node=-1):
        if self.isEmpty(): return False
        if node == -1: node = self.root
        if node == None: return False
        if node.e == e: return True
        return self.contains(e, node.right) if e > node.e else self.contains(e, node.left)

    # 获得长度
    def getSize(self):
        return self.size

    # 是否为空
    def isEmpty(self):
        return self.size == 0