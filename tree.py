class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=Node(10)
root.left=Node(40)
root.right=Node(50)

root.left.left=Node(60)
root.left.right=Node(70)


root.right.left=Node(80)
root.right.right=Node(90)


root.left.left.left=Node(99)
def inorder(node):
     if node is None:
        return
     inorder(node.left)     
     print(node.data,end=" ") 

inorder(root)


def out(node):
    if node is None:
        return
    
     
    print(out(node.right))

out(root)