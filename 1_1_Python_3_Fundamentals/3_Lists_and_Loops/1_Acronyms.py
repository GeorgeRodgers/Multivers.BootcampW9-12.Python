# In Python an array is refferend to as a list
# The first item in a list has an index of 0

# To create a list we can assign it to a varible
# In this case we will be creating a list of strings

acronyms = ['LOL','IDK','SMH']

# At this point we can add items to the end of the list using the '.append()' method

acronyms.append('BFN')
acronyms.append('IMHO')

print(acronyms) # Expected output ['LOL', 'IDK', 'SMH', 'BFN', 'IMHO']

# We can also remove an item from the list with the '.remove()' providing the value as an item

acronyms.remove('BFN')

print(acronyms) # Expected output ['LOL', 'IDK', 'SMH', 'IMHO']

# We can also remove an item based on it's index position, however, the syntax is a little different

del acronyms[2]

print(acronyms) # Expected output ['LOL', 'IDK', 'IMHO']

# We can also check if an item exists with in a list usinf an if statement
# Note the string must be saved to a variable, in this case word

word = 'BFN'

if word in acronyms:
    print(word + ' is in the list.')
else:
    print(word + ' is not in the list.') # Given we have removed BFN from the list, this line is expected to run

# Currently when we print a list, the list is printed in a similar style to how it was created (i.e. in [])
# If we wanted to print each item on a new line we would need a loop
# Below we have a 'for' loop that uses acronym as a tempoary variable, as this is temporary we can call it anything that has not yet been declared
# 'in' directs the loop to our acroynms list

for acronym in acronyms:
    print(acronym) # This will print item of the list on a new line