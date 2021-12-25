# Rules of Recursion:
#     Indetify the base case
#     Identify the recursive case
#     Get closer and closer and return when needed. Usually you will have 2 returns
#  
# Time Complexity is O(N)

def findFactorialRecursive(number) -> int:
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)

def findFactorialIterative(number) -> int:
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

print(findFactorialRecursive(10))
print(findFactorialIterative(5))

def fibonacciIterative(number): # O(N)
    if number <= 1:
        return number
    first = 0
    second = 1
    result = 0
    for _ in range(2, number + 1):
        result = first + second
        first, second = second, result
    
    return result


def fibonacciRecursive(number): # O(2^N)
    if number < 2:
        return number

    return fibonacciRecursive(number - 1) + fibonacciRecursive(number - 2)

print(fibonacciIterative(8))
print(fibonacciRecursive(8))

# Reverse a String using Recursion

def ReverseRecursion(string):
    if string == '':
        return ''
    return ReverseRecursion(string[1:]) + string[0]

print(ReverseRecursion("yoyo mastery"))