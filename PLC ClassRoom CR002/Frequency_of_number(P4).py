# Read a paragraph from the user and count the number of words, the frequency
# of words appearing, and search for a specific word.

# Store a paragraph in a string variable
str = "New Delhi is the Capital of India . \
Bangalore is the capital of Karnataka . \
India is the world's largest Democratic country"

# Print the entered paragraph
print("Entered Paragraph : " + str)

# Split the paragraph into words and count the total number of words
wordsList = str.split()
wordCount = len(wordsList)
print("Total Number of words:", wordCount)

# Create an empty dictionary to store word frequency counts
counts = dict()

# Split the string into a list of words
words = str.split()

# Loop through each word in the list
for word in words:
    if word in counts:
        # If the word already exists in dictionary, increase its count by 1
        counts[word] = counts[word] + 1
    else:
        # Otherwise, add the word to dictionary with initial count 1
        counts[word] = 1

# Print each word and its frequency
for key in list(counts.keys()):
    print(key, ":", counts[key])

# Ask the user to enter a word to search in the paragraph
searchWord = input("\nEnter the word to search: ")

# Use find() method to check if the word exists in the paragraph
result = str.find(searchWord)

if(result != -1):
    # If found, print success message
    print(searchWord + " Word found in Paragraph")
else:
    # If not found, print failure message
    print(searchWord + " !!!!! Word not found in Paragraph")
