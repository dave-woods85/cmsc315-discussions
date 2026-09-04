"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""
from unit2_stacks_queues.unit2_discussion import my_stack


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None



class BST:
    def __init__(self, value=None): # added default value to allow for creation of a BST with a start value
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None
        if value: # if a value is passed, create the root node with that value
            self.root = Node(value)


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        if self.root is None: # if there is not a root, create a Node with this value and make it the root.
            self.root = Node(value)

        else:
            self._insert_recursive(self.root, value) # otherwise trigger the recursive insert method



    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if self.search(value) is None: # Make sure the value isn't already in the tree
            if value < node.value: # designate a left child
                if node.left is None: # check if there is already a left child
                    node.left = Node(value) # assign a new node with the given value
                else:
                    self._insert_recursive(node.left, value) # keep searching for empty node
            else: # make a right child
                if node.right is None: # check if there is already a right child
                    node.right = Node(value) # assign a new node with the given value
                else:
                    self._insert_recursive(node.right, value) # keep searching for empty node
        else:
            print(f"Value ({value}) already exists.") # inform the user that the value already exists in the tree


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        if self.root is not None:
            if self.root.value is value: # if the root of the tree holds the value that is being searched, return the root
                return self.root
            else:
                return self._search_recursive(self.root, value) # begin the recursive search

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None: # check if there is no more nodes to search on this branch
            return None
        elif node.value == value: # see if the current node holds the searched value
            print(f"Found value {value}") # inform the user that the value has been found
            return node
        elif value < node.value: # check which direction to search next
            return self._search_recursive(node.left, value) # search left child
        else:
            return self._search_recursive(node.right, value) # search right child


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        bst_list = [] # initiate an empty list
        if self.root is None: # make sure the tree isn't empty
            return "Tree is empty." # inform the user
        else:
            bst_list = (self._inorder_recursive(self.root, None)) # trigger the recursive list creation
            return bst_list # send the inorder list back

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if values is None: # initiate a list to add too if the list is empty (so it doesn't get erased every time)
            values = []

        if node is not None: # make sure there is a node to grab a value from
            self._inorder_recursive(node.left, values) # check left
            values.append(node.value) # add the value to the list
            self._inorder_recursive(node.right, values) # check right
        else:
            return None # trigger the traversal to stop

        return values # send the list back


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")
    new_bst = BST()
    value_list = [10, 30, 32, 1, 12, 11, 8, 45, 91, 34, 76, 23]
    print(value_list)
    for value in value_list:
        new_bst.insert(value)
    """ 
    Because a BST is ordered in a way where you can always check for a greater than/less than, you can eliminate
    a vast swath of potential values. This drastically reduces the amount of items that needs to be searched.
    """

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")
    print(new_bst.inorder())
    """
    Due to the nature of the sorting for a BST, you can always find the lowest value by traversing down the left side
    of the tree. The next lowest value should then be the parent of that child, then the right child of that parent. The
    recursive traversal is meant to follow this path which orders the values in ascending order.
    """
    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    search_list = [1, 8, 17, 32, 100, 29, 91]
    for value in search_list:
        new_bst.search(value)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    print("Traversing an empty tree")
    empty_bst = BST()
    empty_bst.inorder()
    print("Searching an empty tree")
    empty_bst.search(4)
    print("Inserting duplicate values")
    new_bst.insert(1)
    single_node_bst = BST(15)
    single_node_bst.inorder()

    """
    Nothing bad seems to happen because I tried to handle any cases where there were None values given. I also added
    a default value to the constructor for the BST to allow for an initial value to be given to setup a root node.
    """
    print("===Real-world example=== ")
    print("Alphabetically ordered class list:")
    class_list = BST()
    student_names = ["Fred", "Johnathan", "Timothy", "Dennis", "Robert", "Aaron", "Anthony", "Heather", "Blake", "Nick"]
    for name in student_names:
        class_list.insert(name)
    print(class_list.inorder())




if __name__ == "__main__":
    main()