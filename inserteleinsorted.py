def insert_into_sorted_list(sorted_list, element):
    # Traverse the list to find the correct position for insertion
    position = 0
    for i in range(len(sorted_list)):
        if sorted_list[i] >= element:
            position = i
            break
    else:
        # If the element is greater than all elements in the list
        position = len(sorted_list)
    # Insert the element at the correct position
    sorted_list = sorted_list[:position] + [element] + sorted_list[position:]
    return sorted_list
# Example usage
sorted_list = [1, 3, 4, 7, 9]
element = 0
updated_list = insert_into_sorted_list(sorted_list, element)
print("Updated sorted list:", updated_list)
