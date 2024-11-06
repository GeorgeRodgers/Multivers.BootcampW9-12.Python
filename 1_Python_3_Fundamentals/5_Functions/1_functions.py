# Unlike JavaScript there is only one way to define a function
# This is done using the 'def' keyword
# We can exemplify this by creating a greeting function

def greeting(name):
    print('Hello', name)

# Now the function is defined we can write the main function
# A function must be defined before it is called

userName = input('What is your name?\n')

greeting(userName)