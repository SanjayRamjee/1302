def merge_sort(arr):
    # Base case: when the list is only 1 in length, it is returned
    if len(arr) <= 1:
        return arr

    # List is split into two halves, a right and a left
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Both halves recursively sorted
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Sorted halves are merged together in descending order
    sorted_arr = merge(left_half, right_half)

    return sorted_arr

def merge(left, right):
    # Empty list that will contain the merged list in descending order
    result = []

    left_index = 0
    right_index = 0

    # Comparing values from both lists, larger one is added
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left and right lists 
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    #Merged array is returned
    return result



unsorted_list = [12, 5, 6, 9, 3, 7, 15]
# Variable created that stores the sorted list, then is printed
sorted_list = merge_sort(unsorted_list)
print("Sorted list in descending order: ", sorted_list)
