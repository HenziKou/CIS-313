# Henzi Kou
# Lab 1
# January 23, 2019

from sys import argv

class Node(object):
    def __init__(self, data = None, next = None):
	self.__data = data
	self.__next = next

    def setData(self, data):
	# Set the "data" data field to the corresponding input
	self.__data = data

    def setNext(self, next):
	# Set the "next" data field to the corresponding input
	self.__next = next

    def getData(self):
	# Return the "data" data field
	return self.__data

    def getNext(self):
	# return the "next" data field
	return self.__next


class Queue(object):
    def __init__(self):
	self.__head = None
	self.__tail = None

    def enqueue(self, newData):
	# Create a new node whose data is newData and whose next node is null
	# Update head and tail
	# Hint: Think about what's different for the first node added to the Queue
	n = Node()			# Initialize a new node
	n.setData(newData)		# Assign node with newData value
	n.setNext(None)			# Move pointer to next item which is null

	# Check if queue is empty. If so assign head and tail to same newData.
	if self.isEmpty():
	    self.__head = n
	    self.__tail = n

	# If not, then just assign tail to newData
	else:
	    self.__tail.setNext(n)
	    self.__tail = n

	return None

    def dequeue(self):
	# Return the head of the Queue
	# Update head
	# Hint: The order you implement the above 2 tasks matters, so use a temporary node
	# 	to hold important information
	# Hint: Return null on a empty Queue
	temp = Node()			# Temporary node

	# Check if queue is empty. If so nothing can be returned.
	if self.isEmpty():
	    return None

	# Otherwise fetch the first item in the list
	else:
	    temp = self.__head		# Assign temp to current head node
	    self.__head = self.__head.getNext()		# Set new head to next node
	    return temp

    def isEmpty(self):
	# Check if the Queue is empty
	if self.__head == None:
	    return True

	return False

    def printQueue(self):
	# Loop through your queue and print each Node's data
	current = self.__head

	while current != None:
	    print(current.getData())	# Print the current node data
	    current = current.getNext()	# Move current to next node


class Stack(object):
    def __init__(self):
	# We want to initialize our Stack to be empty
	# (ie) Set top as null
	self.__top = None

    def push(self, newData):
	# We want to create a node whose data is newData and next node is top
	# Push this new node onto the stack
	# Update top
	n = Node()			# Initialize a new node
	n.setData(newData)		# Set data as newData
	n.setNext(self.__top)		# Set next node to be null
	self.__top = n			# Assign top of stack with values of node n

	return None

    def pop(self):
	# Return the Node that currently represents the top of the stack
	# Update top
	# Hint: The order you implement the above 2 tasks matters, so use a temporary node
	# 	to hold important information
	# Hint: Return null on a empty stack
	temp = Node()

	# Check if stack is empty
	if self.isEmpty():
	    return None

	# Otherwise remove topmost item on the stack
	else:
	    temp = self.__top
	    self.__top = self.__top.getNext()	# Set new top item
	    return temp

    def isEmpty(self):
	# Check if the Stack is empty
	if self.__top == None:
	    return True

	return False

    def printStack(self):
	# Loop through your stack and print each Node's data
	# Set current node to top of the stack
	current = self.__top

	# Loop through the stack and print the value
	while current != None:
	    print(current.getData())
	    current = current.getNext()

	return None

class TwoStackQueue(object):
    def __init__(self):
	# Initializing stack head and tail
	#self.__stackhead = 
	pass


def main(argv):
    # Create a Scanner that reads system input
    input_file = argv[1]
    with open(input_file, 'r') as file_ob:
	# Loop over the scanner's input
	# For each line of the input, send it to isPalindrome()
	# If isPalindrome returns true, print "This is a Palindrome."
	# Otherwise print "Not a Palindrome."

	n = int(file_ob.readline().strip())

	# Read each line and pass into isPalindrome function and print respective answer
	for i in range (n):
	    # Take the next line in the file
	    x = file_ob.readline().strip()
	    if isPalindrome(x):			# Is a palindrome
		print("This is a Palindrome.")
	    else:				# Is not a palindrome
		print("Not a Palindrome.")

def isPalindrome(s):
    # Use your Queue and Stack class to test wheather an input is a palindrome
    myStack = Stack()
    myQueue = Queue()

    # Find the length of each string
    size = len(s)

    # Create a boolean variable to identify if string is a palindrome
    is_p = False

    # Enqueue items into queue and push into stack
    for i in range (size):
	myQueue.enqueue(s[i])
	myStack.push(s[i])

    ## Helper function ##
    # print("stack data")
    # myStack.printStack()

    # print("queue data")
    # myQueue.printQueue()

    # Pop and dequeue data to compare if the characters are the same
    for j in range ((size // 2) + 1):
	# Pop and dequeue an element from the stack and queue respectively
	queue_data = myQueue.dequeue().getData()
	stack_data = myStack.pop().getData()

	# Update the boolean variable if characters match
	# If there is just one mismatch then break the string comparision and return false
	if queue_data == stack_data:
	    is_p = True
	else:
	    is_p = False
	    break

    return is_p

def isPalindromeEC(s):
    # Implement if you wish to do the extra credit.return
    pass

if __name__ == "__main__":
    main(argv)


