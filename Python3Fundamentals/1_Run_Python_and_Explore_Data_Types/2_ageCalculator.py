# The reason why we have to define data type coersion in Python is due to it begin a strongly typed language.
# This means that a value will not hange in an unexpected way.

# In this example we will have to change the input into an integer using the int() function

age = int(input('How old are you?\n'))

# If we wanted to convert someone ages into decades we could dived it by 10
# However, we if the age is not a multiple of 10 we would get a decimal
# to return the the whole number from the division we can use the '//' opporator

decades = age // 10

# To get the remainder we can '%' use the modulous opperator

years = age % 10

# Again in th print staemtn we need to convert integers into strings so they can be concatenated

print('You are ' + str(decades) + ' decades and ' + str(years) + ' years old.')