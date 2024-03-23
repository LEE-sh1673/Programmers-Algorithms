import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BstTree:
    def __init__(self, parent):
        self.parent = Node(parent)

    
    def insert(self, value):
        def insert_recursively(node, value):
            if node is None:
                return Node(value)

            if node.value > value:
                node.left = insert_recursively(node.left, value)
            else:
                node.right = insert_recursively(node.right, value)
            return node
            
        self.parent = insert_recursively(self.parent, value)

    
    def post_order(self):
        def order(node):
            if node is not None:
                order(node.left)
                order(node.right)
                print(node.value)
                
        order(self.parent)


def post_order(s, e):
    if s > e:
        return

    mid = e + 1
    
    for i in range(s+1, e+1):
        if nodes[s] < nodes[i]:
            mid = i
            break

    post_order(s+1, mid - 1)
    post_order(mid, e)
    print(nodes[s])


sys.setrecursionlimit(10**9)
nodes = list(map(lambda x: int(x.strip()), sys.stdin.readlines()))
post_order(0, len(nodes)-1)
