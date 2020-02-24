# Henzi Kou
# Lab 4
# March 4, 2019

from sys import argv
from RBT import RedBlackTree

def main(argv):

    fileName = argv[1]
    T = RedBlackTree()
    with open(fileName, 'r') as fob:
        for line in fob:
            l = line.strip().split()
            if len(l) == 2:
                command = l[0]
                data = int(l[1].strip())
                if command == 'insert':
                    T.insert(data)
            
                if command == 'delete':
                    T.delete(data)

                # Missing Search Function                    
		if command == 'search':
		    T.search(data)

            if len(l) == 1:
                print(l[0])
                T.traverse(l[0])
                print('')

if __name__ == "__main__":
    main(argv)
