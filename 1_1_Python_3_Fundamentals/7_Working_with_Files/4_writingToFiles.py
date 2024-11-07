# In addition to searching in files we may want to edit them
# Firstly to do this we need to define what we are adding

acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition of ' + acronym +'?\n')

# By default open() uses 'r' as the second parameter, which stand for read
# 'w' stand write and replace the entire file with the new information
# 'a' stands for append and adds information to the end of the file

with open('1_1_Python_3_Fundamentals/7_Working_with_Files/acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n') # .write() method is used to write to the file