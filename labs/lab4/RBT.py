# Henzi Kou
# Lab 4
# March 4, 2019

# BinarySearchTree is a class for a binary search tree (BST)
# when called, a BST is initialized with no root and size 0.
# size keeps track of the number of nodes in the tree
from Node import RB_Node

class RedBlackTree:
    # initialize root and size
    def __init__(self):
        self.root = None
        self.size = 0
        
        # All leaf nodes point to self.sentinel, rather than 'None'
        # Parent of root should also be self.sentinel
        self.sentinel = RB_Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.leftChild = self.sentinel
        self.sentinel.rightChild = self.sentinel

    '''
    Free Methods
    '''

    def sentinel(self):     
        return self.sentinel

    def root(self):
        return self.root

    def __iter__(self):
        # in-order iterator for your tree
        return self.root.__iter__()

    def getKey(self, key):
        # expects a key
        # returns the key if the node is found, or else raises a KeyError

        if self.root:
            # use helper function _get to find the node with the key
            res = self._get(key, self.root)
            if res: # if res is found return the key
                return res.key
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    
    def getNode(self, key):
        # expects a key
        # returns the RB_Node object for the given key
        
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, key not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function _get receives a key and a node. Returns the node with
    # the given key
    def _get(self, key, currentNode):
        if currentNode is self.sentinel: # if currentNode does not exist return None
            # print("couldn't find key: {}".format(key))
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            # recursively call _get with key and currentNode's leftChild
            return self._get( key, currentNode.leftChild )
        else: # key is greater than currentNode.key
            # recursively call _get with key and currentNode's rightChild
            return self._get( key, currentNode.rightChild )

    
    def __contains__(self, key):
        # overloads the 'in' operator, allowing commands like
        # if 22 in rb_tree:
        # ... print('22 found')

        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        # Same as binary tree delete, except we call rb_delete fixup at the end.

        z = self.getNode(key)
        if z.leftChild is self.sentinel or z.rightChild is self.sentinel:
            y = z
        else:
            y = z.findSuccessor()
        
        if y.leftChild is not self.sentinel:
            x = y.leftChild
        else:
            x = y.rightChild
        
        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.leftChild:
                y.parent.leftChild = x
            else:
                y.parent.rightChild = x

        if y is not z:
            z.key = y.key
    
        if y.color == 'black':
            if x is self.sentinel:
		self._rb_Delete_Fixup(y)
	    else:
		self._rb_Delete_Fixup(x)

    def traverse(self, order = "in-order", top = -1):
        # Same a BST traverse
        if top is -1:
            top = self.root
            last_call = True
        
        last_call = False

        if top is not self.sentinel :
            if order == "in-order":
                self.traverse(order, top.leftChild)
                print(top.key),
		# print(top.color)
                self.traverse(order, top.rightChild)

            if order == "pre-order":
                print(top.key),
                self.traverse(order, top.leftChild)
                self.traverse(order, top.rightChild)

            if order == "post-order":
                self.traverse(order, top.leftChild)
                self.traverse(order, top.rightChild)
                print(top.key),

        if last_call:
            print

    '''
    Required Methods Begin Here
    '''

    def insert(self, key):
        # add a key to the tree. Don't forget to fix up the tree and balance the nodes.
	# Initialize nodes x, y, and z
	y = self.sentinel
	x = self.root

	if (self.root == None):
	    # If the root is null then set the root's data value to key
	    self.root = RB_Node(key, self.sentinel, self.sentinel, self.sentinel, "black")

	else:
	    # Else set a new node z to hold the value of key and assign z to the correct location in rb tree
	    z = RB_Node(key, self.sentinel, self.sentinel, self.sentinel, "red")

	    while (x != self.sentinel):
		# While node x is not null assign its data values to node y
		y = x

		if (z.key < x.key):
		    # Assign node x to its left child if node x is greater than node z
		    x = x.leftChild
		else:
		    # Else assign node x to its right child
		    x = x.rightChild

	    z.parent = y

	    if (y == self.sentinel):
		# If y is still the sentinel node, make the root equal to z
		self.root = z
	    elif (z.key < y.key):
		# If node y is greater than node z, assign y's left child to z
		y.leftChild = z
	    else:
		# Else assign y's right child to z
		y.rightChild = z

	    # Use replaceNodeData() function to change node z values
	    z.replaceNodeData(key, self.sentinel, self.sentinel, "red")
	    # Insert node z into _rbInsertFixup() to fix up tree
	    self._rbInsertFixup(z)

	return None

    def _rbInsertFixup(self, z):
        # write a function to balance your tree after inserting
	while (z.parent.color == "red"):
	    # If node z's parent is red then it violates property 4
	    if (z.parent == z.parent.parent.leftChild):
		# Node z is in the left subtree of its grandparent node
		y = z.parent.parent.rightChild

		if (y.color == "red"):
		    # Violation where uncle and z nodes are both red so perform a color change
		    z.parent.color = "black"
		    y.color = "black"
		    z.parent.parent.color = "red"
		    # Move pointer to grandparent node and perform fixup if neccessary
		    z = z.parent.parent
		else:
		    # Violation where uncle and z nodes are NOT both red
		    if (z == z.parent.rightChild):
			# If node z is the right child rotate left, else rotate right, then recolor
			z = z.parent
			self.leftRotate(z)
		    z.parent.color = "black"
		    z.parent.parent.color = "red"
		    self.rightRotate(z.parent.parent)

	    else:
		# Node z is in the right subtree of its grandparent node
		y = z.parent.parent.leftChild

		if (y.color == "red"):
		    # Violation where uncle and z nodes are both red so perform a color change
		    z.parent.color = "black"
		    y.color = "black"
		    z.parent.parent.color = "red"
		    # Move pointer to grandparent node and perform fixup if neccessary
		    z = z.parent.parent
		else:
		    # Violation where uncle and z nodes are NOT both red
		    if (z == z.parent.leftChild):
			# If node z is the left child rotate right, else rotate left, then recolor
			z = z.parent
			self.rightRotate(z)
		    z.parent.color = "black"
		    z.parent.parent.color = "red"
		    self.leftRotate(z.parent.parent)

	self.root.color = "black"		# Maintain property 2

	return None

    def _rb_Delete_Fixup(self, x):
        # receives a node, x, and fixes up the tree, balancing from x.
	while (x != self.root and x.color == "black"):
	    if (x == x.parent.leftChild):
		# When node x is the left child
		w = x.parent.rightChild
		if (w.color == "red"):
		    # Case 1: violation when x's sibiling w is red
		    w.color = "black"
		    x.parent.color = "red"
		    self.leftRotate(x.parent)
		    w = x.parent.rightChild
		if (w.leftChild.color == "black" and w.rightChild.color == "black"):
		    # Case 2: violation when x's sibiling w is black, and both of w's children are black
		    w.color = "red"
		    x = x.parent
		else:
		    if (w.rightChild.color == "black"):
			# Case 3: violation when x's sibiling w is black, w's left child is red, and w's
			# 	  right child is black
			w.leftChild.color == "black"
			w.color = "red"
			self.rightRotate(w)
			w = x.parent.rightChild

		    # Case 4: x's sibiling w is black, and w's right child is red
		    w.color = x.parent.color
		    x.parent.color = "black"
		    w.rightChild.color = "black"
		    self.leftRotate(x.parent)
		    x = self.root
	    else:
		# When node x is the right child
		w = x.parent.leftChild
		if (w.color == "red"):
		    # Case 1: violation when x's sibiling w is red
		    w.color == "black"
		    x.parent.color = "red"
		    self.rightRotate(x.parent)
		    w = x.parent.leftChild
		if (w.leftChild.color == "black" and w.rightChild.color == "black"):
		    # Case 2: violation when x's sibiling w is black, and both of w's children are black
		    w.color = "red"
		    x = x.parent
		else:
		    if (w.leftChild.color == "black"):
			# Case 3: violation when x's sibiling w is black, w's left child is red, and w's
			#	  right child is black
			w.rightChild.color = "black"
			w.color = "red"
			self.leftRotate(w)
			w = x.parent.leftChild

		    # Case 4: x's sibiling w is black, and w's right child is red
		    w.color = x.parent.color
		    x.parent.color = "black"
		    w.leftChild.color = "black"
		    self.rightRotate(x.parent)
		    x = self.root

	x.color = "black"

	return None

    def leftRotate(self, x):
        # perform a left rotation from a given node
	# Set y and turn y's left subtree into x's right subtree
	y = x.rightChild
	x.rightChild = y.leftChild

	if (y.leftChild != self.sentinel):
	    # Assign x to be the parent of y's left child
	    y.leftChild.parent = x

	# Link x's parent to y
	y.parent = x.parent

	if (x.parent == self.sentinel):
	    # Node x is the root node
	    self.root = y
	elif (x == x.parent.leftChild):
	    # Node x is the left child
	    x.parent.leftChild = y
	else:
	    # Node x is the right child
	    x.parent.rightChild = y

	# Assign x as y's left child
	y.leftChild = x
	x.parent = y
        
	return None

    def rightRotate(self, x):
        # perform a right rotation from a given node
	# Set y and turn y's right subtree into x's right subtree
        y = x.leftChild
	x.leftChild = y.rightChild

	if (y.rightChild != self.sentinel):
	    # Assign x to be the parent of y's right child
	    y.rightChild.parent = x

	# Link x's parent to y
	y.parent = x.parent

	if (x.parent == self.sentinel):
	    # Node x is the root node
	    self.root = y
	elif (x == x.parent.rightChild):
	    # Node x is the right child
	    x.parent.rightChild = y
	else:
	    # Node x is the left child
	    x.parent.leftChild = y

	# Assign x as y's right child
	y.rightChild = x
	x.parent = y

	return None


    '''
    Optional handy methods that you can imagine can start here
    '''

    def search(self, key):
	# Public method to the private __contains()__ method
	if (self.__contains__(key) is True):
	    print("Found key: {}".format(key))
	else:
	    print("Couldn't find key: {}".format(key))

	return None





