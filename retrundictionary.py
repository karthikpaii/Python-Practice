
#{number : total number }
def count_frequency(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
    return freq
nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = count_frequency(nums)
print("Frequency of elements:", result) 