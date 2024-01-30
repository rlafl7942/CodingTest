import sys

tree = {}
class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preOrder(node):
    print(node.data, end='')
    if node.left != '.':
        preOrder(tree[node.left])
    if node.right != '.':
        preOrder(tree[node.right])

def inOrder(node):
    if node.left != '.':
        inOrder(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        inOrder(tree[node.right])

def postOrder(node):
    if node.left != '.':
        postOrder(tree[node.left])
    if node.right != '.':
        postOrder(tree[node.right])
    print(node.data, end='')


n = int(input())

for _ in range(n):
    a,b,c = sys.stdin.readline().rstrip().split()
    tree[a] = Node(a,b,c)

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])
