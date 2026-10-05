'''roll_numbers_input = input("Enter roll numbers separated by spaces: ")
a = list(map(int, roll_numbers_input.split()))
roll_number = int(input("Enter the roll number to search: "))
if roll_number in a:
    index = a.index(roll_number)
    print(f"Roll number {roll_number} found at index {index}")
else:
    print(f"Roll number {roll_number} not found in the list")'''

'''a= ['Rice', 'Sugar', 'Milk', 'Oil', 'Soap']
print("the given list is: ", a)
item = input("Enter the item to search: ")
if item in a:
   print(f"{item} is found in the list.")
else:
    print(f"{item} is not found in the list.")'''

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

ids_input = input("Enter sorted employee IDs separated by spaces: ")
employee_ids = list(map(int, ids_input.split()))

target_id = int(input("Enter the employee ID to search: "))
index = binary_search(employee_ids, target_id)

if index != -1:
    print(f"Employee ID {target_id} found at index {index}")
else:
    print(f"Employee ID {target_id} not found in the list")