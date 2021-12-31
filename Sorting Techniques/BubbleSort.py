# Time Complexity  --> O(N^2) --> Nested loop
# Space Complexity --> O(1)   --> As we are not using any additional list

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    for j in reversed(range(len(array))): # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array

bubbleSort(numbers)
print(numbers)