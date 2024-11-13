def fizzbuzz():
    for num in range(1,101):
        if (num % 3 == 0) & (num % 5 == 0):
            print(f'FizzBuzz')
        elif num % 3 == 0:
            print(f'Fizz')
        elif num % 5 == 0:
            print(f'Buzz')
        else:
            print(f'{num}')

fizzbuzz()