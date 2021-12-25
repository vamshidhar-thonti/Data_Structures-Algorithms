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