# In Python, a dictionary is the same as a JavaScript object
# We can define a dictionary with value or empty using '{}'

currentMovies = {'The Grinch': '11:00am',
                 'Rudolph': '1:00pm'}

# We can also add an item by setting a key equal to a new value or using the '.update()' method to append the dictionary with another dictionary
# If the key already exist in the first dictionary the value will be updated

currentMovies['Frosty the Snowman'] = '2:00pm'

currentMovies.update({'Frosty the Snowman': '3:00pm', # In this line the value 'Frosty the Snowman' is updated instead of a new key value pair being created
                      'Christmas Vacation': '5:00pm'})

# Using a loop we can now print the movies that are showing

print("We're showing the following movie:")
for key in currentMovies:
    print(key)

# If we want the user to be able to select, we need to add input and save it to a variable

movie = input('What movie would you like to see?\n')

# To get the movie showtime we must now use the '.get()' method

showtime = currentMovies.get(movie)

if showtime == None: # If the movie is not found, showtime will be set to 'None' and so we should let the user know the movie was not found
    print('Requested movie not found')
else:
    print(movie, 'is playing at', showtime)