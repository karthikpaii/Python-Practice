# Function to perform linear search
def linear_search(data, target):
    # Traverse through all elements in the list
    for index, value in enumerate(data):
        # If the target is found, return the index
        if value == target:
            return index  # Returning the index where the target is found
    return -1  # Return -1 if the target is not found
# Example usage
dataset = [5, 2, 9, 1, 5, 6]
target_value = 9
# Call the linear_search function
result = linear_search(dataset, target_value)
if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found in the dataset.")