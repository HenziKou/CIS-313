# Henzi Kou
# January 16, 2019
# CIS 313
# lab0.py

from sys import argv

def main(argv):
    file_name = argv[1]
    
    with open(file_name, 'r') as file_object:
      numProblems = file_object.readline()

      for line in file_object:
        a, b = line.strip().split(' ')
        the_gcd = gcd(a, b)
        the_lcm = lcm(a, b)
        print("{} {}".format(the_gcd, the_lcm))

def gcd(a, b):
  # Find the greatest common divisor of a and b
  # Hint: Use Euclid's Algorithm
  # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
  
  # Convert inputs from string to int
  a = int(a)
  b = int(b)

  # Euclid's Algorithm from Wikipedia
  while b > 0:
    a, b = b, a % b

  return a

def lcm(a, b):
  # Find the least common multiple of a and b
  # Hint: Use the gcd of a and b
 
  # Convert inputs from string to int
  a = int(a)
  b = int(b)

  return a * b / gcd(a, b)

if __name__ == "__main__":
  main(argv)
