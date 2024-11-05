# We can nest lists and dictionaries within each other in order to create data structures
# We will exemplify this using a contacts list for a group of students

contacts = {
    'number': 3, # Number of students
    'students':
        [
            {'name': 'David Smith', 'email': 'david.smith@email.com'},
            {'name': 'John Doe', 'email': 'john.doe@email.com'},
            {'name': 'Jane Doe', 'email': 'jane.doe@email.com'}
        ]
}

# We can use a loop to get information out of the contacts dictionary
# given the student information is specified in a list with the key student we must direct the loop to it

print('Student email:')
for student in contacts['students']:
    print(student['email']) # Given we only want to return the email list we can specify the key for the student in the list