class TreeNode:
    def __init__(self, key, val = None):
        if val == None:
            val = key

        self.key = key
        self.value = val
        self.left = None
        self.right = None
        


class Tree:
    def __init__(self):
        self.root = None

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def add(self, key, value = None):
        new_node = TreeNode(key, value)
        if self.root == None:
            self.root = new_node
            return

        previous = None
        current = self.root
        while current != None:
            previous = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right

        if key <= previous.key:
            previous.left = new_node
        else:
            previous.right = new_node

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find(self, key):
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    def inorder_helper(self, current, traversal_list):
        if current:
            self.inorder_helper(current.left, traversal_list)
            traversal_list.append(
                {
                    "key": current.key,
                    "value": current.value
                }
            )
            self.inorder_helper(current.right, traversal_list)

    # Time Complexity: O(n)
    # Space Complexity: O(n)?
    def inorder(self):
        traversal_list = []
        self.inorder_helper(self.root, traversal_list)
        print(traversal_list)
        return traversal_list

    def preorder_helper(self, current, traversal_list):
        if current:
            traversal_list.append(
                {
                    "key": current.key,
                    "value": current.value
                }
            )
            self.preorder_helper(current.left, traversal_list)
            self.preorder_helper(current.right, traversal_list)

    # Time Complexity: O(n)
    # Space Complexity: O(n)    
    def preorder(self):
        traversal_list = []
        self.preorder_helper(self.root, traversal_list)
        return traversal_list

    def postorder_helper(self, current, traversal_list):
        if current:
            self.postorder_helper(current.left, traversal_list)
            self.postorder_helper(current.right, traversal_list)
            traversal_list.append(
                {
                    "key": current.key,
                    "value": current.value
                }
            )

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def postorder(self):
        traversal_list = []
        self.postorder_helper(self.root, traversal_list)
        return traversal_list

    def height_helper(self, current, height_list, height):
        if current:
            height += 1
            self.height_helper(current.left, height_list, height)
            self.height_helper(current.right, height_list, height)
        height_list.append(height)

    # Not sure this is the best way to find height
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def height(self):
        height_list = []
        height = 0
        self.height_helper(self.root, height_list, height)
        return max(height_list)


    def bfs_helper(self, current, traversal_list):
        if current:
            if current.left:
                traversal_list.append(
                {
                    "key": current.left.key,
                    "value": current.left.value
                }
            )
            if current.right:
                traversal_list.append(
                {
                    "key": current.right.key,
                    "value": current.right.value
                }
            )
            self.bfs_helper(current.left, traversal_list)
            self.bfs_helper(current.right, traversal_list)

    # This passes the tests, but I'm not sure if it would actually work with a more complex tree...
    # Optional Method
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def bfs(self):
        traversal_list = []
        if self.root:
            traversal_list.append(
                {
                    "key": self.root.key,
                    "value": self.root.value
                }
            )
        self.bfs_helper(self.root, traversal_list)
        return traversal_list


#   # Useful for printing
    def to_s(self):
        return f"{self.inorder()}"
