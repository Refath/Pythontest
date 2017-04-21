# from the system, we import the arguments
from sys import argv

# the two arguments are the script, and the filename
script, filename = argv

# open the filename that was entered as the second argument
txt = open (filename)

# print the name of the file, substitute with the argument
print "Here's your file %r:" % filename
# read the the file
print txt.read()

# prompt the user to type the file again
print "Type the filename again:"
# store user input as filename
file_again = raw_input ("> ")

# set a variable name for the input, and open that filename
txt_again = open (file_again)

# read the filename
print txt_again.read()
