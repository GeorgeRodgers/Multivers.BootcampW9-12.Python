# The first thing we want to do with a loan calculator is get some some information from our use about there loan

owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input('What what will your monthly payment be, in dollar?\n'))
months = int(input('How many months do you want to see the results for?\n'))
monthly_rate = apr / 100 / 12

# Using a for loop we can repeat the code below for the number of months the user wants to see

for i in range(months): # range requires an integer and so the number of months is coveted on line 6

    # Calculate monthly interest paid
    interest_paid = owed * monthly_rate

    # Monthly interest added to amount owed
    owed += interest_paid

    # We can add an if statement in order to avoid paying more of the loan than need and calculate the final payment of the loan and what month it will be paid

    if (owed - payment < 0):
        print('Month', i+1)
        print('Your final payment is $', format(owed, ".2f"), '.', sep = '')
        break # This stops the loop if the conditional statement is made

    #Payment made
    owed -= payment

    print('Month', i+1)
    print('You paid $', format(payment, ".2f"), ' of which $', format(interest_paid, ".2f"), ' was interest.', sep = '', end = ' ') # By default print appends an argument with a new line, setting end to a space prints the next comment on the same line
    print('You now owe $', format(owed, ".2f"), '.\n', sep = '')