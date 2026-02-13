# List of students' records as tuples (Name, Marks) 
students = [ 
("Ravi", 78), 
("Sneha", 85), 
("Arjun", 92), 
("Meena", 88), 
("Kiran", 95) 
] 
# Sort the list by marks in descending order 
sorted_students = sorted(students, key=lambda x: x[1], reverse=True) 
# Display the sorted list 
print("Students sorted by marks:") 
for name, marks in sorted_students: 
    print(name, ":", marks) 
# Topper will be the first student in the sorted list 
topper = sorted_students[0] 
print("\nTopper is:", topper[0], "with", topper[1], "marks") 
