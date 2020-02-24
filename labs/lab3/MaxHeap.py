# Henzi Kou
# Lab 3
# March 3, 2019

class MaxHeap(object):

    def __init__(self, size):
        # finish the constructor, given the following class data fields:
        #   self.__maxSize
        #   self.__length
        #   self.__heap
        self.__maxSize = size
        self.__length = 0
        self.__heap = [None] * size

	''' free helper functions '''
    def getHeap(self):
        return self.__heap    

    def getMaxSize(self):
        return self.__maxSize
    
    def setMaxSize(self, ms):
        self.__maxSize = ms
        # May need to add more code here if you want to use this method

    def getLength(self):
        return self.__length
    
    def setLength(self, l):
        self.__length = l
    
    ''' Required Methods '''
    def insert(self, data):
    	# Insert an element into your heap.
    	
    	# When adding a node to your heap, remember that for every node n, 
    	# the value in n is greater than or equal to the values of its children, 
    	# but your heap must also maintain the correct shape.
        
        # Increase heap size and set new index with value of data
        self.setLength(self.getLength() + 1)
        i = self.getLength()

        self.__heap[i] = data

        # While index is greater than 1 and the value is greater than its parent
        # exchange the parent value with the new value
        while (i > 1 and self.__heap[self.__getParent(i)] < self.__heap[i]):
            tmp = self.__heap[self.__getParent(i)]
            self.__heap[self.__getParent(i)] = data
            self.__heap[i] = tmp

            # Now set index to parent index to check that it maintains max-heap
            # property
            i = self.__getParent(i)
        
        return None
    
    def maximum(self):
        # return the max value in the heap
        return self.__heap[1]

    def extractMax(self):
        # remove and return the maximum value in the heap
        # If heap is empty then we have a heap underflow error
        if (self.__length < 1):
            print("Error: heap underflow")
            return None

        # Store max value into a variable to return later
        maxNode = self.__heap[1]

        # Reassign first item in heap as the last item
        self.__heap[1] = self.__heap[self.getLength()]
        # Resets last index node to be null
        self.__heap[self.getLength()] = None
        # Delete last index node
        self.setLength(self.getLength() - 1)

        # Now heapify to maintain max-heap property
        self.__heapify(1)

        return maxNode
    
    def __heapify(self, node):
    	# helper function for reshaping the array
        # Get the left and right indexes of node
        l_index = self.__getLeftChild(node)
        r_index = self.__getRightChild(node)

        # Get the left and right values
        left = self.__heap[l_index]
        right = self.__heap[r_index]

        # If left child is bigger then set it temporarily as the index with the
        # largest value
        if ((l_index <= self.getLength()) and (left > self.__heap[node])):
            largest = l_index

        # Else the current node is the largest
        else:
            largest = node

        # If the right child is larger than the largest value then set it as the
        # index with the largest value
        if ((r_index <= self.getLength()) and (right > self.__heap[largest])):
            largest = r_index

        # Now swap values to maintain max-heap property
        if (largest != node):
            tmp = self.__heap[largest]
            self.__heap[largest] = self.__heap[node]
            self.__heap[node] = tmp

            # Now heapify node at largest index to maintain max-heap property
            self.__heapify(largest)

        return None

    ''' Optional Private Methods can go after this line '''
    # If you see yourself using the same ~4 lines of code more than once...
    # You probably want to turn them into a method.

    def __getParent(self, i):
        # Returns the index of the parent node 
        return i // 2

    def __getLeftChild(self, i):
        # Returns the index of the left child
        return 2 * i

    def __getRightChild(self, i):
        # Returns the index of the right child
        return (2 * i) + 1







