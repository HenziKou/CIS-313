# Henzi Kou
# Lab 3
# March 3, 2019

from sys import argv
from pQueue import pQueue

def main(argv):
    # Loop over input file. 
    # Split each line into the task and the corresponding number (if one exists)
    # Depending on what the input task was, preform the corresponding function
    # Finally, close your file.
    inputFile = argv[1]

    # Open file once to count number of lines
    f_in = open(inputFile, "r")
    count = 0

    # Count the number of lines to pass into as the max heap size
    for line in f_in:
    	count += 1

    # Close file
    f_in.close()

    # Open file a second time to run through pQueue and MaxHeap functions
    file = open(inputFile, "r")
    pQ = pQueue(count)

    # Loop through each line and perform corresponding task
    for line in file:
    	line = line.strip("\n")
    	task = line.split()

    	# If task is insert
    	if (task[0] == "insert"):
    		val = int(task[1])
    		pQ.insert(val)

    	# Else if task is print
    	elif (task[0] == "print"):
    		pQ.printQueue()

    	# Else if task is isEmpty
    	elif (task[0] == "isEmpty"):
    		# If empty print empty
    		if (pQ.isEmpty()):
    			print("Empty")

    		# Else print not empty
    		else:
    			print("Not Empty")

    	# Else if task is maximum
    	elif (task[0] == "maximum"):
    		print(pQ.maximum())

    	# Else if task is extractMax
    	elif (task[0] == "extractMax"):
    		print(pQ.extractMax())

    file.close()



if __name__ == "__main__":
    main(argv)
