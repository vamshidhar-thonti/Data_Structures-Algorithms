# Time Complexity  --> O(N^2) --> Nested loop
# Space Complexity --> O(1)   --> As we are not using an additional list

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    for i in range(len(array)):
        low = i
        for j in range(i, len(array) - 1):
            if array[low] > array[j + 1]:
                low = j + 1
        array[i], array[low] = array[low], array[i]

    return array

selectionSort(numbers)
print(numbers)