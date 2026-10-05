def binary_search_with_steps(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, steps


marks_input = input("Enter sorted marks separated by spaces: ")
marks = list(map(int, marks_input.split()))


target_mark = 78
index, steps = binary_search_with_steps(marks, target_mark)

if index != -1:
    print(f"Mark {target_mark} found at index {index}")
    print(f"Number of steps taken: {steps}")
else:
    print(f"Mark {target_mark} not found in the list")
    print(f"Number of steps taken: {steps}")