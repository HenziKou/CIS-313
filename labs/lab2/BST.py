from Node import Node

class BST(object):
    def __init__(self):
        self.__root = None

    def getRoot(self):
        # Private Method, can only be used inside of BST.
        return self.__root

    def __findNode(self, data):
        # Private Method, can only be used inside of BST.
        # Search tree for a node whose data field is equal to data.
        # Return the Node object
        node = self.__root

        # If node is null or node is equal to data then return node
        if (node == None) or (data == node.getData()):
            return node

        # If data value is less than the current node then search the left subtree
        if (data < node.getData()):
            return self.__findNode(node.getLeftChild, data)

        # Else search the right subtree
        else:
            return self.__findNode(node.getRightChild, data)

    def exists(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # If root node is null return false
        if (self.__root == None):
            return False

        # Initialize the current node
        node = self.__root

        # If 
        while (node != None):
            # If node contains data in the tree then return true
            if (node.getData() == data):
                return True

            # If data is less than the current node value then set node to its left child
            if (data < node.getData()):
                node = node.getLeftChild()

            # Else set node to its right child
            else:
                node = node.getRightChild()

        return False

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error

        # Check that root node is not null, else assign it a new value
        if (self.__root == None):
            self.__root = Node(data)
            return

        # Initialize the new temporary and current nodes
        node = self.__root
        node2 = None

        # Go down left or right subtree depending on the comparision of the data value
        while (node != None):
            node2 = node

            # If new node value is less than current node then set current node to its left
	    # child.
            if (data < node.getData()):
                node = node.getLeftChild()

            # Else if set current node to its right child
            elif (data > node.getData()):
                node = node.getRightChild()

            # Else just return
            else:
                return None

        # Then set the parent node
        node = Node(data)
        node.setParent(node2)

        # If data is less than current node then set as the left child of the current node
        if (data < node2.getData()):
            node2.setLeftChild(node)

        # Else place as right child
        else:
            node2.setRightChild(node)

	return None

    def __transplant(self, u, v):
        # Used to move subtrees around as a helper function to delete
        # If u is the root of the tree
        if (u.getParent() == None):
            self.__root = v

        # If u is the left child then it gets updated
        elif (u.getData() == u.getParent().getLeftChild().getData()):
            u.getParent().setLeftChild(v)

        # If u is the right child
        else:
            u.getParent().setRightChild(v)

        # Update the parents of v if v is not null
        if (v != None):
            if (v.getParent() == None):
                v.setParent(u.getParent())

	return None

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change
	# the tree.
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove 
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() to find the successor
	# 	when there are two children
        node = self.__findNode(data)                    # Find the node
        l_node = node.getLeftChild()                    # Find the left child
        r_node = node.getRightChild()                   # Find the right child

        # If there does not exists a left child exchange the placement with the parent
        if (l_node == None):
            self.__transplant(self, node, r_node)

        # If there does not exists a right child exchange the placement with the parent
        elif (r_node == None):
            self.__transplant(self, node, l_node)

        # If there exists two children then use __findSuccessor helper method to find
	# replacement.
        else:
            # Find the successor of the right subtree
            s_node = self.__findSuccessor(r_node)

            # If successor node is null then just return
            if (s_node == None):
                return

            # Exchange placement of the successor node with its right child
            if (s_node.getParent() != node):
                self.__transplant(s_node, s_node.getRightChild())
                s_node.setRightChild(r_node)
                s_node.getRightChild().setParent(s_node)

            # Set l_node as the left child of the successor
            # Set successor as the parent of the left child the successor
            self.__transplant(node, s_node)
            s_node.setLeftChild(l_node)
            s_node.getLeftChild().setParent(s_node)

        return None

    def __findSuccessor(self, aNode):
        # If right subtree is nonempty then use minimum helper function to find leftmost node       
        tmp = aNode

        # If right child exists traverse to the right
        if (tmp.getRightChild() != None):
            tmp = tmp.getRightChild()

            # If left child exists then traverse to the leftmost node
            while (tmp.getLeftChild() != None):
                tmp = tmp.getLeftChild()

            return tmp

        # Else traverse to the left
        tmp = tmp.getLeftChild()

        # Then if node is not null then traverse to the rightmost node
        if (tmp != None):
            while (tmp.getRightChild() != None):
                tmp = tmp.getRightChild()

        return tmp


    def traverse(self, order, top):
        # traverse the tree by printing out the node data for all node in a specified order

        if (top is not None):
            if (order == "preorder"):
                # Traverse tree in preorder
                
                print(top.getData())
                self.traverse("preorder", top.getLeftChild())
                self.traverse("preorder", top.getRightChild())
            
            elif (order == "inorder"):
                # Traverse tree in inorder

                self.traverse("inorder", top.getLeftChild())
                print(top.getData())
                self.traverse("inorder", top.getRightChild())

            elif (order == "postorder"):
                # Traverse tree in postorder

                self.traverse("postorder", top.getLeftChild())
                self.traverse("postorder", top.getRightChild())
                print(top.getData())
            
            else:
                print("Error, order {} undefined".format(order))

	return None




# HINT: Tackling order for the project
#	- Insert
#	- findNode
# 	- Traverse
# 	- Delete


