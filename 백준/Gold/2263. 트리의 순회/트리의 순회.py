from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
nodeNum = [0] * (n + 1)

for i in range(n):
    nodeNum[inorder[i]] = i


def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    root = postorder[postEnd]
    left_nodes = nodeNum[root] - inStart
    right_nodes = inEnd - nodeNum[root]

    print(root, end=" ")
    preorder(inStart, inStart + left_nodes - 1, postStart, postStart + left_nodes - 1)
    preorder(inEnd - right_nodes + 1, inEnd, postEnd - right_nodes, postEnd-1)


preorder(0, n-1, 0, n-1)
