# Basic error handling in Python is very similar to JavaScript
# Instead try/catch we use try/except
# We can exemplify this using the basic acronyms dictionary below

acronyms = {'LOL':'laugh out loud',
            'IDK':"I don't know",
            'SMH': 'Shake my head'}

# If we ran the code below we would get the following error "KeyError: 'BTW'" and our program would stop
# definition = acronyms['BTW']

# Instead we can wrap the code in a try/except statement

try:
    definition = acronyms['BTW']
except:
    print('The key does not exist') # Now an error message is printed to the console and the program keeps running
finally:
    print('Our finally statement will always run wether or not the exception is called') # A finally statement can be added wether or not the exception is called

print('The program is still running')