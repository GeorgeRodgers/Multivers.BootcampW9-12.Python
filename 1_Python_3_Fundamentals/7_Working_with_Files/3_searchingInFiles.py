# When using files we would rarely want to print there content
# We are more likely to be looking for data in them

# We need to define what we are searching for

find = input('What acronym would you like to look up?\n')

found = False # Global variable to check if found
with open('acronyms.txt') as file:
    for line in file: # Search each line of the file
        if find in line: # Check if acronym is included in the line
            print(line) # Print line
            found = True 
            break # Stop loop
    if not found:
        print('Acronym not found') # Print statement if error not found