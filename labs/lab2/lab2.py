# Henzi Kou
# Lab 2
# Feburary 6, 2019

from sys import argv
from BST import BST

def main(argv):
	# Loop over input file (filename passed via argv).
	# Split each line into a task and number (if one exists) 
	#   hint: use the split method for strings https://docs.python.org/2/library/string.html#string.split
	# Perform the function corresponding to the specified task
	# i.e., insert, delete, inorder, preorder, postorder
	# Close the file when you're done.
	filename = argv[1]
	file = open(filename, "r")

	bst = BST()

	for line in file:
		line = line.strip('\n')
		task = line.split(" ")

		# If task is insert
		if (task[0] == "insert"):
			val = int(task[1])
			bst.insert(val)

		# If task is delete
		elif (task[0] == "delete"):
			val = int(task[1])
			bst.delete(val)

		# If task is inorder
		elif (task[0] == "inorder"):
			bst.traverse(task[0], bst.getRoot()) 

		# If task is preorder
		elif (task[0] == "preorder"):
			bst.traverse(task[0], bst.getRoot())

		# If task is postorder
		elif (task[0] == "postorder"):
			bst.traverse(task[0], bst.getRoot())

	# Close file
	file.close()

if __name__ == "__main__":
    main(argv)

