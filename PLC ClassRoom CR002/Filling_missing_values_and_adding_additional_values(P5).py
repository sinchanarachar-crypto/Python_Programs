# Create a sequence with some missing values
sequence = [1, None, 3, 4, None, 6, 7, 8, None, 10]
print("Original Sequence:", sequence)

# Fill in missing values
filled_sequence = []
for num in sequence:
    if num is None:
        filled_sequence.append(0)   # replacing None with 0
    else:
        filled_sequence.append(num)  # keep the original value

print("After Filling Missing Values:", filled_sequence)

# Remove certain numbers from the sequence
# Let's say we want to remove 4 and 7
numbers_to_remove = [4, 7]
cleaned_sequence = []

for num in filled_sequence:
    if num not in numbers_to_remove:
        cleaned_sequence.append(num)

print("After Removing Certain Numbers:", cleaned_sequence)

# Add additional values to enhance the sequence
# Let's add [99, 100, 101] at the end
extra_values = [99, 100, 101]

enhanced_sequence = cleaned_sequence + extra_values

print("Final Enhanced Sequence:", enhanced_sequence)
