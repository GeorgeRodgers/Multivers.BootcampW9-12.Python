# We sort a list of value in the expenses variable

expenses = [10.50, 8, 5, 15, 20, 5, 3]

# Python is similar to JavaScript and requires us to define a sum variable to add the expenses to in th loop

sumTotal = 0

for x in expenses:
    sumTotal += x

# Separating values in a print argument with a comma instead of concatenating doesn't require data coercion
# However, be default value are separated by a space, this can be changed by defining 'sep'

print('You spent $', sumTotal, sep = '')

# Alternatively we can use the 'sum()' function that can take a list as an argument

total = sum(expenses)

print('Using the sum function we can see the total is also $', total, sep = '')