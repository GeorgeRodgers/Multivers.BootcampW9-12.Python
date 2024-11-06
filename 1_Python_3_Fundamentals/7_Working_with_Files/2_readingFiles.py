# There is a test file called acronyms.txt with the same relative path as this one

# It is important to remember to close files when working with them in Python
# This can be done by using the 'with' keyword or wrapping the file handling in a try/finally statement and calling the '.close()' method in the finally statement

# because of the folder structuring of this module the file is located at "C:\Users\mrgeo\Desktop\Multiverse\Bootcamp\Week9-12\Multivers.BootcampW9-12.Python\acronyms.txt"

with open('acronyms.txt') as file:
    # data = file.read() # This return returns the list as a single sting
    # print(data)
    
    # This returns each line of the file in the form of a list
    for line in file:
        print(line) # Now the lines a individually printed to the console
