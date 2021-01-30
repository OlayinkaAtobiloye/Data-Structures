
def counter(start, stop):
    """The counter function counts down from start to stop when start is bigger than stop,
    and counts up from start to stop otherwise."""
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"


def even_numbers(maximum):
    """The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2,
    up to and including the maximum that's passed into the function."""
    return_string = ""
    for x in range(1, maximum+1):
        if x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


def digits(n):
    """The function digits(n) returns how many digits the number has."""
    digit = str(n)
    return len(digit)


def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1


def string_test(sentence):
    """This function accepts sentence(s) in string form as parameter and calculates the number of uppercase
     and lowercase letters in the string."""
    uppercase = 0
    lowercase = 0
    try:
        for letter in sentence:
            if letter.isalpha() and letter.isupper():
                uppercase += 1
            elif letter.isalpha() and letter.islower():
                lowercase += 1
        return 'Number of Lowercase letters is ' + str(lowercase) + '\nNumber of Uppercase letters is ' + str(uppercase)
    except (TypeError, ValueError):
        return 'Enter a string input'


print(string_test('The quick Brown Fox'))
print(string_test('My name is Sodiq Agunbiade, I am your tutor for this cohort'))
print(string_test('You are a Student of 30daysofcode'))


def unique(L):
    """This function takes a list that contains numbers as parameters and returns a sorted new list
    with unique elements of the first list
     """
    unique_list = []
    for i in L:
        if i not in unique_list:
            unique_list.append(i)
        else:
            pass
    return print('Sample List: {}'.format(L) + '\nUnique List: {}'.format(sorted(unique_list)))


unique([1, 2, 3, 3, 3, 3, 4, 5])
unique([1, 2, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 4, 5, 6, 6, 11, 22, 33, 44])
unique([1, 2, 3, 3, 3, 3, 4, 5, 5, 3, 3, 3, 3, 4, 5, 6, 6, 110, 20, 19, 34])


def primeSum(num):
    """This function takes in an integer number and prints the sum of prime numbers
    between 1 and the integer"""
    prime_sum = 0
    if 1 < num < 1000000:
        for number in range(2, num):
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime_sum += number
    return prime_sum


print(primeSum(10))
print(primeSum(20))
print(primeSum(100))


def fibonacci(number):
    """This function checks if a number is in the fibonacci sequence and returns True if
     true and False otherwise"""
    import math
    p = (1 + (math.sqrt(5)))/2
    q = (1 - (math.sqrt(5)))/2
    fn = 0

    try:
        if number < 0:
            return 'fibonacci({})==Wrong input'.format(number)
        else:
            for n in range(0, number):
                if number == 2:
                    return 'fibonacci({})==True'.format(number)
                elif fn < number:
                    fn = int(((p ** n) - (q ** n)) / (math.sqrt(5)))
                elif fn == number:
                    return 'fibonacci({})==True'.format(number)
                else:
                    return 'fibonacci({})==False'.format(number)
    except (ValueError, TypeError):
        return 'fibonacci({})==Invalid'.format(number)


def squareSum(n):
    """This function returns the difference between sum of square and square of sum
    of natural numbers"""
    try:
        sum_of_square = (n * (n + 1) * (2 * n + 1)) / 6
        square_of_sum = ((n * (n + 1)) / 2) ** 2
        if n < 0:
            return 'squareSum({})==Wrong Input'.format(n)
        else:
            dif = int(square_of_sum - sum_of_square)
            return 'squareSum({0})=={1}'.format(n, dif)

    except (TypeError, ValueError):
        return 'squareSum({})==Invalid!'.format(n)


def OddEven(num):
    """This function determines whether the addition of the digits of a number
    are odd or even"""
    add = 0
    if type(num) is not int:
        raise TypeError('Enter an integer')
    else:
        for i in str(num):
           add += int(i)

    if add % 2 == 0:
        return 'Evenish'
    else:
        return 'Oddish'


def fastSum(n):
    """This function returns the sum of first n terms"""
    return n * (n + 1) / 2


def averageMultiple(num):
    """
    This function takes in a number between 1 and 1000 and returns the average multiples of 3 and 5 in the number
    """
    try:
        num is int
        sum_of_multiples = 0
        count = 0
        if 1 < num < 5000:
            for numbers in range(2, num):
                if numbers % 3 == 0:
                    sum_of_multiples += numbers
                    count += 1
                elif numbers % 5 == 0:
                    sum_of_multiples += numbers
                    count += 1
                else:
                    pass
        else:
            return ("Number should be between 1 and 5000")
        return sum_of_multiples / count
    except TypeError:
        return ("Please enter an integer")


print(averageMultiple(10))
print(averageMultiple(20))
print(averageMultiple("7"))
print(averageMultiple(6000))


