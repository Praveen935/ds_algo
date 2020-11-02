class Node(object):

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent=parent

class Tree(object):
    def __init__(self):
        self.root = None

    def iterative_insert(self, value):
        root = self.root
        curr_node = None
        while root:
            curr_node = root
            if value < root.value:
                root = root.left
            else:
                root = root.right

        node = Node(value, parent=curr_node)
        if curr_node:
            if node.value < curr_node.value:
                curr_node.left = node
            else:
                curr_node.right = node
        else:
            self.root = node

    def recursive_insert(self, root, value):
        if root is None:
            node = Node(value)
            self.root = node
            return
        if root.value == value:
            return

        if value < root.value:
            if root.left is None:
                node = Node(value, parent=root)
                root.left = node
            else:
                self.recursive_insert(root.left, value)
        else:
            if root.right is None:
                node = Node(value, parent=root)
                root.right = node
            else:
                self.recursive_insert(root.right, value)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def search(self, value):
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                return curr_node
            else:
                if value < curr_node.value:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

    def minimum(self, node):
        curr_node = node
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def maximum(self, node):
        curr_node = node
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node

    def predeccessor(self, node):
        '''
        The maximum value before this node in the in order traversal
        if left child - maximum value in left subtree
        traverse to parent until first right turn or none
        '''
        if node.left:
            return self.maximum(node.left)
        current_node = node
        parent = current_node.parent
        while parent and current_node == parent.left:
            current_node = parent
            parent = current_node.parent
        return parent

    def successor(self, node):
        """
        the minimum value after this node in inorder traversal
        if right subtree - minimum of right subtree
        else traverse to parent until first left turn
        """
        if node.right:
            return self.minimum(node.right)
        current_node = node
        parent = current_node.parent
        while parent and current_node == parent.right:
            current_node = parent
            parent = current_node.parent

        return parent

    def successor_without_using_parent_variable(self, node):
        if node.right:
            return self.minimum(node.right)

        return self.succ_recurse(node, self.root, None)

    def succ_recurse(self, node, current_node, parent):
        if not current_node:
            return None
        # TODO

    def is_balanced(self, root):
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height-right_height) > 1:
            return False
        else:
            return self.is_balanced(root.left) and self.is_balanced(root.right)

    def height(self, node):
        if not node:
            return 0
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return 1+max((left_h, right_h))

    def balanced(self, root):
        left_h = 0
        right_h = 0
        if root is None:
            return True

        l = self.balanced(root.left)
        r = self.balanced(root.right)

        if abs(left_h - right_h) <= 1:
            return l and r

            # if we reach here then the tree
            # is not balanced
        return False

    def traverse(self, root):
        if not root:
            return 0

        print("===========traversing: recurse node: %s" %root.value)

        left = self.traverse(root.left)
        if left == -1:
            return -1

        right = self.traverse(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(right, left)

    def isBalanced(self, root) -> bool:
        print("traversing node: %s" % root.value)
        if self.traverse(root) == -1:
            return False
        return True



if __name__ == "__main__":
    t = Tree()
    # node_count = int(input())
    # while node_count > 0:
    #     node_count -= 1
    #     val = int(input())
    #     t.recursive_insert(t.root, val)

    values = [5, 3, 1,2, 4, 7, 9, 8]
    # values = [5, 3, 1, 2, 4]
    values = [8, 6, 7, 5, 2, 3, 4]
    values = [6,2,8,0,4,7,9,3,5]
    values = [3,9,20,5,7]

    # for val in values:
    #     t.iterative_insert(val)
    node1=Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)

    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)


    t.root = node1
    node1.left = node2
    node1.right=node8

    node2.left = node3
    node2.right=node5

    node3.left = node4
    node5.right = node6


    node8.left=node9
    node8.right = node10
    node10.right=node11

    node11.left=node12
    node11.right=node13


    # node = t.search(5)
    # print("========minimum: %s" %t.minimum(node).value)
    # print("========maximum: %s" % t.maximum(node).value)
    # succ = t.successor(node)
    # if succ:
    #     print("===========succesor :: %s" %succ.value)
    #
    print("height of the tree : %s " %t.isBalanced(t.root))

