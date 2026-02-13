# Program to swap two variables without using a temp variable

x = int(input("Enter the value for X: "))
y = int(input("Enter the value for Y: "))

# Swapping without temp
x, y = y, x

print("\nX and Y values after swapping:")
print("x =", x)
print("y =", y)
