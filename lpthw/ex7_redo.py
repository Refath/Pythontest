from sys import argv

script, filename = argv

print "Hey! Here's your file: %r" % filename
txt = open (filename)

print txt.read()

print "Tell me the file again, please?"
file_again = raw_input (">> ")

txt_again = open (file_again)

print txt_again.read()
