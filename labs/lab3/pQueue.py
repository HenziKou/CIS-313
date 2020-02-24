# Henzi Kou
# Lab 3
# March 3, 2019

from MaxHeap import MaxHeap

class pQueue(object):
    def __init__(self, size) :
        # Build the Constructor
        self.__myHeap = MaxHeap(size)

    def insert(self, data):
        self.__myHeap.insert(data)
        
    def maximum(self):
        return self.__myHeap.maximum()
    
    def extractMax(self):
        return self.__myHeap.extractMax()

    def isEmpty(self):
        # Return true when the priority queue is empty
        return self.__myHeap.getLength() == 0
    
    def printQueue(self):
        # followed by each element separated by a comma. 
        # Do not add spaces between your elements.
        #
        # (Optional; python gives us ~*~ magic methods ~*~ and there happens to 
        # be one for strings (def __str__) You can replace this method (printQueue)
        # with the magic method __str__, and use it to return the string 
        # representation of your Queue if it pleases you.)

        length = self.__myHeap.getLength() + 1

        # Initialize an empty string to store value of heap
        s = ""

        # Loop through the elements of the heap and print
        for i in range(1, length):
            # Adds a comma after every element besides the last one
            if (i < length - 1):
                s += str(self.__myHeap.getHeap()[i])
                s += ","

            # Prevents the addition of an extra unwanted comma
            else:
                s += str(self.__myHeap.getHeap()[i])

        # Print the final string
        print("Current Queue: {}".format(s))

        return None

    def __str__(self):
        # Print the elements of the heap
        pass

    
