class TreeNode:
    def __init__(self, parent, left, right, value):
        """
            Description:
                initializes a new node
            Parameters:
                parent: the parent of the node
                left: the left child of the node
                right: the right child of the node
                value: the value of the node
            Return:
                None
        """
        self.value = value
        self.parent = parent
        self.left_child = left
        self.right_child = right

    def set_value(self, value):
        """
            Description:
                sets the value of the node
            Parameters:
                value: the new value of the node
            Return:
                None
        """
        self.value = value

    def is_external(self) -> bool:
        """
            Description:
                returns True if the node is external; False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.left_child is None and self.right_child is None

    def is_internal(self) -> bool:
        """
            Description:
                returns True if the node is internal; False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return not self.is_external()
    
    def __str__(self):
        """
            Description:
                returns the string representation of the node
            Parameters:
                None
            Return:
                str
        """
        return str(self.value)
    
    def ancestors(self) -> list:
        """
            Description:
                returns the ancestors of the node
            Parameters:
                None
            Return:
                str
        """
        if self.parent is None:
            return [self]
        else:
            return [self] + self.parent.ancestors()
    
    def __repr__(self):
        """
            Description:
                returns the string representation of the node
            Parameters:
                None
            Return:
                str
        """
        return self.__str__()
    
    def node_depth(self) -> int:
        """
            Description:
                returns the depth of the node
            Parameters:
                None
            Return:
                int
        """
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.node_depth()
        
    def non_recursive_node_depth(self) -> int:
        """
            Description:
                returns the depth of the node non-recursively
            Parameters:
                None
            Return:
                int
        """
        depth = 0
        current_node = self

        while current_node.parent is not None:
            depth += 1
            current_node = current_node.parent

        return depth

    def node_height(self) -> int:
        """
        Description:
            returns the height of the node
        Parameters:
            None
        Return:
            int
        """
        if self.left_child is None and self.right_child is None:
            return 0
        elif self.left_child is None:
            return 1 + self.right_child.node_height()
        elif self.right_child is None:
            return 1 + self.left_child.node_height()
        else:
            return 1 + max(self.left_child.node_height(), self.right_child.node_height())

class BinaryTree:
    def __init__(self):
        """
            Description:
                initializes an empty binary tree
            Parameters:
                None
            Return:
                None
        """
        self.root = None
        self.size = 0

    def get_size(self) -> int:
        """
            Description:
                returns the number of nodes in the tree
            Parameters:
                None
            Return:
                int
        """
        return self.size
    
    def is_empty(self) -> bool:
        """
            Description:
                returns True if the tree is empty; False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.size == 0
    
    def add_root(self, value):
        """
            Description:
                adds a root node to the tree
            Parameters:
                value: int
                    -the value of the new root node
            Return:
                TreeNode object
        """
        if self.root is not None:
            raise ValueError("BinaryTree.add_root: root is already initialized.")
        
        self.root = TreeNode(None, None, None, value)
        self.size += 1

        return self.root
    
    def add_left(self, parent, value):
        """
            Description:
                adds a left child node to the tree
            Parameters:
                parent: TreeNode object
                    -the parent of the new left child node
                value: int
                    -the value of the new left child node
            Return:
                TreeNode object
        """
        if not parent.left_child is None:
            raise ValueError("BinaryTree.add_left: parent.left_child is already initialized.")
        
        parent.left_child = TreeNode(parent, None, None, value)
        self.size += 1

        return parent.left_child

    def add_right(self, parent, value):
        """
            Description:
                adds a right child node to the tree
            Parameters:
                parent: TreeNode object
                    -the parent of the new right child node
                value: int
                    -the value of the new right child node
            Return:
                TreeNode object
        """
        if not parent.right_child is None:
            raise ValueError("BinaryTree.add_right: parent.right_child is already initialized.")
        
        parent.right_child = TreeNode(parent, None, None, value)
        self.size += 1
        
        return parent.right_child
    
    def _recursive_str(self, r, level):
        """
            Description:
                returns the string representation of the tree
            Parameters:
                r: TreeNode object
                    -the root node of the tree
            Return:
                str
        """
        #base case: the tree is empty
        if r is None:
            return ""
        
        #without intermediate variables
        return level * "  " + str(r) + "\n" + self._recursive_str(r.left_child, level + 1) + "\n" + self._recursive_str(r.right_child, level + 1)
        
    def __str__(self):
        """
        Description:
            returns the string representation of the tree
        Parameters:
            None
        Return:
            str
        """
        return self._recursive_str(self.root, 0)
        
    def tree_height(self) -> int:
        """
            Description:
                returns the height of the tree
            Parameters:
                None
            Return:
                int
        """
        if self.root is None:
            return 0
        
        left_height = self.root.left_child.node_height()
        right_height = self.root.right_child.node_height()

        return 1 + max(left_height, right_height)
    
    def node_depth(self, node) -> int:
        """
            Description:
                returns the depth of the node
            Parameters:
                node: TreeNode object
                    -the node whose depth is to be returned
            Return:
                int
        """
        if node is None:
            raise ValueError("BinaryTree.node_depth: Node is empty.")
        
        return node.node_depth()
    
    def print_ancestors(self, node):
        return node.ancestors()
    
    def print_breadth_first(self):
        queue = []
        queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(str(current_node))
            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)

    def reverse_breadth_first(self):
        queue = []
        stack = []
        queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            stack.append(current_node)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)
            if current_node.left_child is not None:
                queue.append(current_node.left_child)

        while len(stack) > 0:
            pass
    
    def _print_post_order_helper(self, r):
        #base case: the tree is empty
        if r is None:
            return
        
        #print left subtree
        self._print_post_order_helper(r.left_child)

        #print right subtree
        self._print_post_order_helper(r.right_child)

        #print root
        print(str(r))

    def print_post_order(self):
        print(self._print_post_order_helper(self.root))

# def test_ancestors():
#     bt = BinaryTree()
#     root = bt.add_root(5)
#     r_left = bt.add_left(root, 10)
#     r_right = bt.add_right(root, 11)
#     bt.add_left(r_right, 7)
#     r_left_left = bt.add_left(r_left, 8)
#     r_left_left_left = bt.add_left(r_left_left, 2)
#     bt.add_left(r_left_left_left, 9)
#     bt.add_right(r_left_left, 10)

#     assert bt.print_ancestors(root) == [root]
#     assert bt.print_ancestors(r_left) == [r_left, root]
#     assert bt.print_ancestors(r_left_left_left) == [r_left_left_left, r_left_left, r_left, root]

# def test_node_depth():
#     bt = BinaryTree()
#     root = bt.add_root(5)
#     r_left = bt.add_left(root, 10)
#     r_right = bt.add_right(root, 11)
#     bt.add_left(r_right, 7)
#     r_left_left = bt.add_left(r_left, 8)
#     r_left_left_left = bt.add_left(r_left_left, 2)
#     bt.add_left(r_left_left_left, 9)
#     bt.add_right(r_left_left, 10)

#     print(bt.node_depth(root))

#     assert bt.node_depth(root) == 0
#     assert bt.node_depth(r_left) == 1
#     assert bt.node_depth(r_left_left) == 2

# def preorder_output(node):
#     if len(node.children):
#         return ""
    
#     result = str(node) + "\n"
#     result += preorder_output(node.left_child)
#     result += preorder_output(node.right_child)
    
#     return result

# tree = BinaryTree()
# one = tree.add_root(1)
# two = tree.add_left(one, 2)
# three = tree.add_right(one, 3)
# four = tree.add_left(two, 4)
# tree.add_right(two, 5)
# tree.add_left(four, 7)
# tree.add_right(four, 8)
# six = tree.add_left(three, 6)
# tree.add_left(six, 9)
# tree.add_right(six, 10)
# print(preorder_output(tree.root))
# print(tree)
# print(tree.tree_height())