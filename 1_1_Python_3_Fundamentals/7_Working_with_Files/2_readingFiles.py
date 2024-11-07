# There is a test file called acronyms.txt with the same relative path as this one

# It is important to remember to close files when working with them in Python
# This can be done by using the 'with' keyword or wrapping the file handling in a try/finally statement and calling the '.close()' method in the finally statement

with open('1_1_Python_3_Fundamentals/7_Working_with_Files/acronyms.txt') as file:
    # data = file.read() # This return returns the list as a single sting
    # print(data)
    
    # This returns each line of the file in the form of a list
    for line in file:
        print(line) # Now the lines a individually printed to the console
