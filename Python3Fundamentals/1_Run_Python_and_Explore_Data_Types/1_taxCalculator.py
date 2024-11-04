# Unlike JavaScript, we do not need to define if a variable is variable or a constant before defining it.
# In the UK VAT is set at 20% so we can use 0.2 for out tax calculator

vat = 0.2

# We would like some input from our user so we can use the inpunt() that takes a variable as a argument and uses it as a prmopt.
# input() defaults to give the input as a string, so we must use coersion to change the input to a float 

amount = float(input('What is the price without VAT?\n'))

# We can now caluclate the amount of VAT paid and add it to give the total price.

total = amount + amount*vat

# We can log the amount to the console with a message
# Using the format() function to coerse the float to have 2 decimal places
# Unlike JavaScript python does not force coertion when differeent data types are combined
# In this case the flaot is converted into a string

print('The total amount, including VAT, is £ ' + str(format(total, ".2f")) + '.')