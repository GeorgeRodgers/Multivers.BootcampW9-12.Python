# If we want to get the user input to create a list we could write out the following code

    # expenses = []
    # expenses.append(float(input('Enter an expense: \n')))
    # expenses.append(float(input('Enter an expense: \n')))
    # expenses.append(float(input('Enter an expense: \n')))
    # expenses.append(float(input('Enter an expense: \n')))
    # expenses.append(float(input('Enter an expense: \n')))
    # expenses.append(float(input('Enter an expense: \n')))
    # expenses.append(float(input('Enter an expense: \n')))
    # total = sum(expenses)
    # print('You spent $', total, sep = '')

# However this inefficient, so instead we should loop through
# To set the number of iterations of the loo we can use the 'range()' function
# This take the argument start, stop step, by default start is 0 and step is 1
# i.e. range(x) is the same as range(0, x, 1)

# The loop code is written below
# We can also allow the user to in put how many expenses they would like to add

num_expenses = int(input("How may expenses to your have?\n"))

expenses = []
for i in range(num_expenses):
    expenses.append(float(input('Enter an expense: \n')))

total = sum(expenses)
print('You spent $', total, sep = '')