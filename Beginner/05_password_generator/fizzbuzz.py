# Write your code below this row 👇
numbers = range(1, 101)

for number in numbers:

    if number % 3 != 0 and number % 5 != 0:
        print(number)

    elif number % 3 == 0 and number % 5 != 0:
        print('Fizz')

    elif number % 5 == 0 and number % 3 != 0:
        print('Buzz')

    else:
        print('FizzBuzz')
