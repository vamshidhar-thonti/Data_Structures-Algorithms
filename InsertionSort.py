# Time Complexity  --> O(N^2) --> Nested loop
# Space Complexity --> O(1)   --> As we are not using an additional list

# If the given input is small or if its nearly sorted,
#     Insertion sort is the best and can be acheived in  O(N)

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    for i in range(0, len(array)):
        if array[i] < array[0]:
            temp = array[i]
            del array[i]
            array.insert(0, temp)
            # print('first ', array)
        else:
            for j in range(1, i):
                if array[i] > array[j-1] and array[i] < array[j]:
                    temp = array[i]
                    del array[i]
                    array.insert(j, temp)
                    # print(array)

    return array

insertionSort(numbers)
print(numbers)