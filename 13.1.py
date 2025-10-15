def linear_search(roll_numbers, target):
    for roll in roll_numbers:
        if roll == target:
            return True
    return False

# Function for Binary Search
def binary_search(sorted_roll_numbers, target):
    low = 0
    high = len(sorted_roll_numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_roll_numbers[mid] == target:
            return True
        elif sorted_roll_numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Step 1: Get list of roll numbers from the user
raw_input = input("Enter all registered roll numbers (separated by space or comma): ")

# Convert input string into list of integers
registered_students = [int(x) for x in raw_input.replace(',', ' ').split()]

# Step 2: Get the roll number to search
target_roll = int(input("Enter the roll number to verify registration: "))

# Step 3: Perform both searches
found_linear = linear_search(registered_students, target_roll)
sorted_students = sorted(registered_students)
found_binary = binary_search(sorted_students, target_roll)

# Step 4: Display the result
print("\n--- Search Results ---")
print(f"Linear Search: Roll number {target_roll} {'is Registered' if found_linear else 'is NOT Registered'}.")
print(f"Binary Search: Roll number {target_roll} {'is Registered' if found_binary else 'is NOT Registered'}.")

