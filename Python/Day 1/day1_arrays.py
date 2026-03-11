print("DSA Journey Started!")
# Day 1 - Arrays and Lists in Python
# =====================================

# 1 - Create and access
numbers = [10, 20, 30, 40, 50]
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")

# 2 - Traverse
for num in numbers:
    print(num)

# 3 - Find max and min manually (without built-in)
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def find_min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

print(f"Max: {find_max(numbers)}")
print(f"Min: {find_min(numbers)}")

# 4 - Reverse array manually
def reverse_array(arr):
    return arr[::-1]

print(f"Reversed: {reverse_array(numbers)}")

# 5 - Find if element exists
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Found {target} at index {i}"
    return f"{target} not found"

print(linear_search(numbers, 30))
print(linear_search(numbers, 99))

# 6 - Find second largest number without using sort()
def find_second_largest(arr):
    if len(arr) < 2:
        return "Array too small"
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

print(f"Second Largest: {find_second_largest(numbers)}")
