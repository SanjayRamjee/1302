file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read: ', len(words))
def binary_search(arr, target):
    left, right = 0, len(words)-1
    iterations = 0

    while left <= right:
        mid = (left + right)//2
        iterations += 1

        if arr[mid] == target:
             print(f"Target = {target} , Found at index = {mid}, Number of iterations = {iterations}")
             return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    mid = -1
    print(f"Target = {target} found at index {mid}, Number of iterations = {iterations}")
    

target = input('Enter search key: ').lower()
while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()