def quick_sort(arr, start, end):
    if start < end:
        print(f"------ Quick sorting from index: {start} to {end} -----")
        print(f"Array segment before partitioning: {arr[start:end+1]}", end=", ")
        pivot_index = partition(arr, start, end)
        print(f"Pivot: {arr[pivot_index]}")
        print(f"Array segment after partitioning: {arr[start:pivot_index]} {arr[pivot_index]} {arr[pivot_index+1:end+1]}")
        
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [11, 12, 1, 9, 6, 5, 4, 7]
quick_sort(arr, 0, len(arr) - 1)
print('The final sorted array', arr)
